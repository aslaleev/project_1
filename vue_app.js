new Vue({
    el: '#app',
    data:{
        naimenovaniya: 'Виды отчета:',
        selected: '',
        date1:'',
        date2:'',
        spisok:[],
        man:[],
        man2:[],
        ud:0,
        inputdata:[],
        hz:[],
        filename:'export_file',
        id:0
    },
    mounted() {
        this.tasklist();
        if(localStorage.date1) this.date1 = localStorage.date1;
        if(localStorage.date2) this.date2 = localStorage.date2;
    },
    watch:{
    date1(newDate1) {
      localStorage.date1 = newDate1;
    },
    date2(newDate2) {
      localStorage.date2 = newDate2;
    }
    },

    methods:{
        tasklist(){
           axios.get(`http://127.0.0.1:5000/todo/api/v1.0/taskslist`)
                .then(response => {
                    this.spisok = response.data.tasks
                })
                .catch(function (error) {
                    console.log(error);
                })
                .finally(() => { this.reRender()});           
        },
        reRender(){
            this.$forceUpdate()
        },
        onChange(event) {
           this.date1 = '';
           this.date2 = '';
           localStorage.clear()
           for (i of event.target.value) {
                if (i=='.'){
                    break;
                }
                id = i;
           }
            axios.get(`http://127.0.0.1:5000/todo/api/v1.0/tasks/${id}`)
            .then(response => {
                this.man = response.data
                console.log(this.man)
            })
            .catch(function (error) {
                console.log(error);
            })
            .finally(() => { this.reRender()});   
        },
        downloadURL(url) {
            var hiddenIFrameID = 'hiddenDownloader',
                iframe = document.getElementById(hiddenIFrameID);
            if (iframe === null) {
                iframe = document.createElement('iframe');
                iframe.id = hiddenIFrameID;
                iframe.style.display = 'none';
                document.body.appendChild(iframe);
            }
            iframe.src = url;
        },
        exportFile() {
            axios.get(`http://127.0.0.1:5000/todo/api/v1.0/export/${this.man}/${this.date1}/${this.date2}`)
            .then(response => {
                localStorage.clear();
                axios.get(`http://127.0.0.1:5000/todo/api/v1.0/tasks/${response.data}`)
                .then(response => {
                    this.downloadURL(`http://127.0.0.1:5000/todo/api/v1.0/uploads/${response.data}`)
                })

            })

        },
    }
})
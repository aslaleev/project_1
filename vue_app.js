new Vue({
    el: '#app',
    data:{
        naimenovaniya: 'Виды отчета:',
        selected: '',
        spisok:[],
        man:[],
        ud:0,
        inputdata:[],
        hz:[],
        filename:'export_file'
    },
    mounted() {
        this.tasklist();
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
//            console.log(event.target.value)
            axios.get(`http://127.0.0.1:5000/todo/api/v1.0/tasks/${event.target.value}`)
            .then(response => {
                this.man = response.data
                console.log(this.man)
            })
            .catch(function (error) {
                console.log(error);
            })
            .finally(() => { this.reRender()});   
        },

        CreateExcel(event){
            console.log(event.target.value)
            axios.get(`http://127.0.0.1:5000/todo/api/v1.0/export/${this.inputdata[0]}/${this.inputdata[1]}`)
            .then(response => {
                this.hz = response.data
                console.log(this.hz)
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
//        exportFile() {
//            axios.get(`http://127.0.0.1:5000/todo/api/v1.0/tasks/name`)
//            .then(response => {
//                this.downloadURL(`http://127.0.0.1:5000/todo/api/v1.0/uploads/${response.data}`)
//            })
//        },
        exportFile() {
            axios.get(`http://127.0.0.1:5000/todo/api/v1.0/export/${this.inputdata[0]}/${this.inputdata[1]}`)
            .then(response => {
                this.downloadURL(`http://127.0.0.1:5000/todo/api/v1.0/tasks/name`)
                .then(response => {
                    this.downloadURL(`http://127.0.0.1:5000/todo/api/v1.0/uploads/${response.data}`)
                })

            })

        },
    }
})
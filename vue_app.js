new Vue({
    el: '#app',
    data:{
        naimenovaniya: 'Виды отчета:',
        selected: '',
        spisok:[],
        man:[],
        ud:0
        
    },
    mounted() {
        this.tasklist();
    },
    methods:{
        tasklist(){
            axios.get('http://127.0.0.1:5000/todo/api/v1.0/taskslist')
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
            ud = event.target.value
            console.log(ud)
            
            axios.get('<div>http://127.0.0.1:5000/todo/api/v1.0/tasks/{{ud}}</div>')
            .then(response => {
                    
                this.man = response.data
                console.log(man)

                
            })
            .catch(function (error) {
                console.log(error);
            })
            .finally(() => { console.log(this.man) ;this.reRender()});   
        }
    },
})
new Vue({
    el: '#app',
    data:{
        naimenovaniya: 'Виды отчета:',
        selected: '',
        spisok:[],
        man:{id:1,"name": 'Vlad' ,"age": 20, param1:'', param2:'второй'}
        
    },
    mounted() {
        this.tasklist();
    },
    methods:{
        tasklist(){
            axios.get('http://127.0.0.1:5000/todo/api/v1.0/taskslist')
                .then(response => {
                    
                    this.spisok = response.data.tasks
                    console.log(spisok)    
                    
                })
                .catch(function (error) {
                    console.log(error);
                })
                .finally(() => {console.log(this.spisok); this.reRender()});           
        },
        reRender(){
            this.$forceUpdate()
        }
    },
})
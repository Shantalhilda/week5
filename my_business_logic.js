const myDb= require('../model/my_db');

//function getting all students
const getStudents = ()=>{
    returnmyDb;
}


//getting student by id
const getStudentById = (request)=> {
    for(i= 1; i < 5; i++ ){
        if(request.params.studentId==myDb.students[i].id){
            return myDb[i];
        }
        console.log(myDb[i]);
    }
    return 'FOUND NOTHING';
};

module.exports ={getStudents, getStudentById}
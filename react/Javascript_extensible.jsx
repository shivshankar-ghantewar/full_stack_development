import React from "react";
// jsx use to write javascript in html

const Shiv=({course,fees,city,education,genai={}})=>{
    const name="shiv";
    const num=2;

    const student={
        "name":"shiv",
        "Age":23,
        "role":"full stack developer"
    }

    console.log(genai);
    return(
        <div>
        <div>my name is {name}</div>
        <h4>jsx use to write javascript in html</h4>
        <div>{4+4}</div>
        <div>{num*5}</div>
        <div className="h1 text-danger">student name={student.name}</div>
        <div className="fw-bold">student Age={student.Age}</div>
        <div className="border border-4 border-success">student role={student.role}</div>
        <div>student course={course}</div>
        <div>course fees ={fees}</div>
        {city && <h3>city={city}</h3>}
        {education && <h3>Education={education}</h3>}
        {genai.llm &&
        <>
        <h1 className="text-success">gen ai syllabus:</h1>
             <br /> {genai.llm} <br /> {genai.Rag} <br /> {genai.vectordb}  <br /></>}
        <button className="btn btn-primary font-3">click me </button>
        </div>
    )
}

export default Shiv; 
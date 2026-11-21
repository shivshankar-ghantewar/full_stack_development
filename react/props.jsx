import React from 'react'
import Shiv from './Javascript_extensible'

const Student = () => {
  const genai={
    "llm":"large language model",
    "Rag":"retrival_Augumented Generation",
    "vectordb": "vector database"

  }
  return (
    <div>
        {/* props use render to another component in component */}
     <Shiv course="python full stack" fees={35000} city="pune" education="MCA"/>
     <Shiv course="gen ai  full stack" fees={70000} genai={genai}/>
    </div>
  )
}

export default Student;

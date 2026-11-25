import React, { useState } from 'react'

const Form_handling = () => {
    // const [name, setname] = useState('')
    // const [email, setemail] = useState('')
    // const [password, setpassword] = useState('')

    const [formdata, setformdata] = useState({
        name:'',
        email:'',
        password:'',
        phone:''
    })

    const onsubmithandler = (e) => {
        e.preventDefault();
    }

    const changehandler=(e)=>{
        const {name,value}=e.target; // destructuring
        setformdata({...formdata,[name]:value})  // rest operator
      
    }

    return (
        <div>
            <form onSubmit={onsubmithandler}>
                <div>
                    name:- <input type="text" name='name' value={formdata.name} onChange={changehandler} />
                </div> <br />
                <div>
                    Email:- <input type="email" name='email'  value={formdata.email} onChange={changehandler} />
                </div> <br />
                <div>
                    password:- <input type="password" name='password' value={formdata.password} onChange={changehandler} />
                </div> <br />
                <div>
                    phone:- <input type="number" name='phone' value={formdata.phone} onChange={changehandler} />
                </div> <br />

                <input type="submit" value="submit" />
            </form>
        </div>
    )
}

export default Form_handling

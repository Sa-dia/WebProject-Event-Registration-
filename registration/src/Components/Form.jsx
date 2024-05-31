import React from "react";
import { useState, useEffect } from "react";
// import Validation from "./Validation";

export default function Form() {
    const initialValues = { fullname:"", email: "", password: "",phonenumber:""};
  const [formValues, setFormValues] = useState(initialValues);
  const [formErrors, setFormErrors] = useState({});
  const [isSubmit, setIsSubmit] = useState(false);
    // const [errors, setErrors] = useState({})
    const [numGuests, setNumGuests] = useState(2);
    const [totalPayment, setTotalPayment] = useState(0);
    const costPerHead = 5000;

    
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValues({ ...formValues, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setFormErrors(validate(formValues));
    setIsSubmit(true);
  };

  useEffect(() => {
    console.log(formErrors);
    if (Object.keys(formErrors).length === 0 && isSubmit) {
      console.log(formValues);
    }
  }, [formErrors]);
  const validate = (values) => {
    const errors = {};
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/i;
    if(!values.fullname)
    {
        errors.fullname = "Name is required!"; 
    }
    // if (!values.username) {
    //   errors.username = "Username is required!";
    // }
    if (!values.email) {
      errors.email = "Email is required!";
    } else if (!regex.test(values.email)) {
      errors.email = "Incorrect e-mail";
    }
    if (!values.password) {
      errors.password = "Password is required";
    } else if (values.password.length < 4) {
      errors.password = "Password must be more than 4 characters";
    } else if (values.password.length > 10) {
      errors.password = "Password cannot exceed more than 10 characters";
    }
    // if(values.confirmpassword==="" || values.confirmpassword!==values.password)
    // {
    //     errors.confirmpassword = "Password is not matched";
    // }
    return errors;
  };

    const handleAmount = (event) => {
        const newValue = event.target.value;
        setNumGuests(newValue);

        const newTotal = costPerHead + (newValue * costPerHead);
        setTotalPayment(newTotal);
    }

    return(
        <div className="signup_container w-100 d-flex justify-content-center">
            <div className="signup_form mt-5 w-50">
                <h1>Registration Form</h1>
                
                <div className="form mt-3">
                    <form className="border p-3" onSubmit={handleSubmit}>
                        <label for="name" className="form-label mt-2">Name</label>
                        <input type="text" placeholder="Enter your name"  className="form-control" onChange={handleChange} value={formValues.fullname} />
                        <p>{formErrors.fullname}</p>

                        <label for="email" className="form-label mt-2">E-mail</label>
                        <input type="email" placeholder="Enter your e-mail"  className="form-control" onChange={handleChange} />
                        <p>{formErrors.email}</p>

                        <label for="password" className="form-label mt-2">Password</label>
                        <input type="password" placeholder="Enter your password" className="form-control" onChange={handleChange} />
                        <p>{formErrors.password}</p>

                        <label for="batch" className="form-label mt-2">Batch</label>
                        {/* <input type="number" placeholder="Enter your batch" className="form-control" min={1} max={31} required/> */}
                        <select className="form-select" required>
                            <option selected disabled value="">---</option>
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                            <option>6</option>
                            <option>7</option>
                            <option>8</option>
                            <option>9</option>
                            <option>10</option>
                            <option>11</option>
                            <option>12</option>
                            <option>13</option>
                            <option>14</option>
                            <option>15</option>
                            <option>16</option>
                            <option>17</option>
                            <option>18</option>
                            <option>19</option>
                            <option>20</option>
                            <option>21</option>
                            <option>22</option>
                            <option>23</option>
                            <option>24</option>
                            <option>25</option>
                            <option>26</option>
                            <option>27</option>
                            <option>28</option>
                            <option>29</option>
                            <option>30</option>
                            <option>31</option>
                        </select> 

                        <label for="contactNum" className="form-label mt-2">Contact no.</label>
                        <input type="number" placeholder="01*********" className="form-control" value={formValues.phonenumber} onChange={handleChange}/>

                        <label for="bloodgroup" className="form-label mt-2">Blood Group</label>
                        <select className="form-select" required>
                            <option selected disabled value="">---</option>
                            <option>A+</option>
                            <option>B+</option>
                            <option>AB+</option>
                            <option>O+</option>
                            <option>A-</option>
                            <option>B-</option>
                            <option>AB-</option>
                            <option>O-</option>
                        </select>

                        <label for="guests" className="form-label mt-2">Number of Guests</label>
                        <select className="form-select" onChange={handleAmount} required>
                            <option>0</option>
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                        </select>

                        <label for="totalAmount" className="form-label mt-2">Total amount to be paid</label>
                        <input type="number" className="form-control" value={totalPayment} /> 

                        <label for="paymentMethod" className="form-label mt-2">Select Payment Method</label>
                        <select className="form-select" required>
                            <option selected disabled value="">---</option>
                            <option value="cash">Cash</option>
                            <option value="bkash">Bkash</option>
                            <option value="nagad">Nagad</option>
                            <option value="rocket">Rocket</option>
                            <option value="card">Card</option>
                        </select>

                        <label for="trxid" className="form-label mt-2">Transaction ID</label>
                        <input type="text" className="form-control" placeholder="Enter your TrxID"/>

                        <button class="fluid ui button blue">Cancel</button>
                        <button class="fluid ui button blue">Submit</button>

                    </form>
                </div>
            </div>
            {Object.keys(formErrors).length === 0 && isSubmit ? (
        <div className="ui message success">Registration Successful!</div>
      ) : (
        // <pre>{JSON.stringify(formValues, undefined, 2)}</pre>
        <p1></p1>
      )}
        </div>
    )


}
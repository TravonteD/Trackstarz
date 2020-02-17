import React from 'react'
import Header from './Header.js'

function CreateAccount() {
  return (
    <div className='app'>
      <Header/>
      <React.Fragment>
        <div className='container'>
          <div className='form-group create-user-form col-sm-12 col-lg-4'>
            <h1 className='login-form__title'>CREATE AN ACCOUNT</h1>
            <input 
              className='form-control create-user-form__input' 
              type='text' 
              id='create-user-form--username' 
              name='username' 
              placeholder='username' />
            <input 
              className='form-control create-user-form__input' 
              type='text' 
              id='create-user-form--email' 
              name='email' 
              placeholder='email' />
            <input 
              className='form-control create-user-form__input' 
              type='password' 
              id='create-user-form--password' 
              name='password' 
              placeholder='password' />
            <button 
              onClick={create_user}
              className='btn btn-primary create-user-form__btn' 
              type='submit'>
            CREATE ACCOUNT
            </button>
          </div>
        </div>
      </React.Fragment>
    </div>
  )
}

function create_user() {
  // const username = document.getElementById('create-user-form--username').value
  // const email = document.getElementById('create-user-form--email').value
  // const password = document.getElementById('create-user-form--password').value
  
  // TODO
  // Make the api call to api/users/new
  // Login as the user
  // Update the global state and redirect on success
  // Invalidate on failure
}

export default CreateAccount;

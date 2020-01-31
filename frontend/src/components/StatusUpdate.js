import React from 'react';

function StatusUpdate() {
  return (
    <div className='status__card'>
    <h4 className='status__card--title'>Update Status</h4>
    <input className='status__card--input' cols='40' rows='10' type='textarea' placeholder='Please Enter the description'/>
    <button className='status__card--submit'>Post</button>
    <button className='fa fa-camera status__card--upload'>upload</button>
    </div>
  )
}

export default StatusUpdate;

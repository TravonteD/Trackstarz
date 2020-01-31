import React from 'react';
import card from '../images/New-Trackstarz-App-logo.png';

function ProfileLeft() {
  return (
    <div className='col-lg-3 col-sm-12'>
    <div className='imagecard'>
    <div className='imagecard__content'>
    <img className='imagecard__img' src={card} alt={'card'}/>
    <h4 className='imagecard__title'>Tray</h4>
    <p className='imagecard__at'>@tray</p>
    </div>
    </div>
    <div>
    </div>
    </div>
  )
}

export default ProfileLeft;

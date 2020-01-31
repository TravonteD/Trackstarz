import React from 'react';
import card from '../images/New-Trackstarz-App-logo.png';

function ProfileRight() {
  return (
    <div className='col-lg-3 col-sm-12'>
    <div className='featured'>
    <h4 className='featured__title'>Featured</h4>
    <img className='featured__img' src={card} alt={'card'}/>
    <img className='featured__img' src={card} alt={'card'}/>
    </div>
    </div>
  )
}

export default ProfileRight;

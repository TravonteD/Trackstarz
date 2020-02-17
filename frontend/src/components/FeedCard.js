import React from 'react';
import profilepic from '../images/sean.jpg'

function FeedCard() {
  return (
    <div className='feed__card'>
      <div className='feed__headline'>
        <img className='feed__headline--img' src={profilepic} alt={'profile'}/>
        <a className='feed__headline--name' href='#' >sean</a>
        <a className='feed__headline--at'  href='#' >@sean</a>
        <small className='feed__headline--date'>4 months, 1 week ago</small>
      </div>
      <div className='feed__content'>
        <p className='feed__content--text'>testing react again</p>
      </div>
      <div className='feed__likestats'>
        <li className='feed__likestats--item'>1 like</li>
      </div>
      <div className='feed__likebar'>
        <li className='feed__likebar--item'>like</li>
        <li className='feed__likebar--item'>comment</li>
        <li className='feed__likebar--item'>share</li>
      </div>
    </div>
  )
}

export default FeedCard;

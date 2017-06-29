import React from 'react'

import '../../styles/tense-page.css'

export default function TensePage () {
  return (
    <div className='tense-page'>
      <div>
        <h2>Present Simple</h2>
        <hr />
        <div className='content'>
          <div className='content-headers'>
            <span>Affirnative</span>
            <span>Negative</span>
            <span>Interrogative</span>
          </div>
          <div className='content-text'>
            <span>I go</span>
            <span>I don't go</span>
            <span>Do I go?</span>
          </div>
          <div className='content-text'>
            <span>You go</span>
            <span>You don't go</span>
            <span>Do you go?</span>
          </div>
          <div className='content-text'>
            <span>He/She/It go<span className='red'>es</span></span>
            <span>He/She/It do<span className='red'>es</span>n't go</span>
            <span>Do<span className='red'>es</span> he/she/it go?</span>
          </div>
          <div className='content-text'>
            <span>We/They go</span>
            <span>We/They don't go</span>
            <span>Do we/they go?</span>
          </div>
        </div>
      </div>

      <div>
        <h2>Past Simple</h2>
        <hr />
        <div className='content'>
          <div className='content-headers'>
            <span>Affirnative</span>
            <span>Negative</span>
            <span>Interrogative</span>
          </div>
          <div className='content-text'>
            <span>I played</span>
            <span>I didn't play</span>
            <span>Did I play?</span>
          </div>
          <div className='content-text'>
            <span>You played</span>
            <span>You didn't play</span>
            <span>Did you play?</span>
          </div>
          <div className='content-text'>
            <span>He/She/It played</span>
            <span>He/She/It didn't play</span>
            <span>Did he/she/it play?</span>
          </div>
          <div className='content-text'>
            <span>We/They played</span>
            <span>We/They didn't play</span>
            <span>Did we/they play?</span>
          </div>
        </div>
      </div>

      <div>
        <h2>Future Simple</h2>
        <hr />
        <div className='content'>
          <div className='content-headers'>
            <span>Affirnative</span>
            <span>Negative</span>
            <span>Interrogative</span>
          </div>
          <div className='content-text'>
            <span>I'll play</span>
            <span>I won't play</span>
            <span>Will I play?</span>
          </div>
          <div className='content-text'>
            <span>You'll play</span>
            <span>You won't play</span>
            <span>Will you play?</span>
          </div>
          <div className='content-text'>
            <span>He/She/It will play</span>
            <span>He/She/It won't play</span>
            <span>Will he/she/it play?</span>
          </div>
          <div className='content-text'>
            <span>We/They will play</span>
            <span>We/They won't play</span>
            <span>Will we/they play?</span>
          </div>
        </div>
      </div>
    </div>
  )
}

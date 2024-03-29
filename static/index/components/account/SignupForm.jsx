import { useEffect, useState } from "react";
import Form from "../../../blocks/Form";
import ThirdParty from "./ThirdParty";
import { ajax } from "jquery";
import { getCookie } from "../../../general/cookies";

export function SignupForm() {
    const [tag, setTag] = useState("")
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [verify_password, setVerificationPassword] =useState("")
    const [remember, setRemember] = useState(true)
    const [headerData, setHeaderData] = useState("")
    const [tagAlert, setTagAlert] = useState(false);
    
    function onSubmit() {
        {
            ajax(location.origin + "/api/account/signup",
            {
                method: 'POST',
                headers: {
                    "X-CSRF-Token": getCookie("csrf")
                },
                data: {
                    tag: tag,
                    username: username,
                    password: password
                }
            }
            ).done(function(response) {
                setHeaderData(response.data)
            }).fail(function(error) {
                console.log(error)
            })
        }

    }

    function checkTagAvailibility(val) {
        if(val == null)
            return
        ajax(location.origin + "/api/account/signup/tag", 
            {
                data: {
                    tag: val
                },
                statusCode: {
                    302: function(response, status, xhr) {
                        setTagAlert(true)
                    },
                    200: function(response, status, xhr) {
                        setTagAlert(false)
                    }
                }
            }, 
        ).done(function(response, xhr) {
            
        }).fail(function(error) {
            
        })
    }

    // This gets the CSRF header info for this form
    useEffect(() => {
        ajax(location.origin + "/api/account/signup"
        ).done(function(response) {
            setHeaderData(response.data)
        }).fail(function(error) {
            console.log(error)
        })
    }, [])

    console.log(tagAlert)

    return <>
        <header>
            <a>
                <b>Create a New Account</b>
            </a>
        </header>
        <Form onSubmit={() => onSubmit()}>
            <input type="text" required={true} maxLength="Username length cannot be longer than 64 characters." data-val-length-max="64" placeholder="Username" id="username" name="username" value={username} onChange={e => setUsername(e.target.value)} />
            <input type="text" required={true} maxLength="Tag length cannot be longer than 64 characters." data-val-length-max="64" placeholder="Tag" id="tag" name="tag" value={tag} onChange={e => {setTag(e.target.value);checkTagAvailibility(e.target.value)}} />
            {
                tagAlert ?
                <div className="alert">
                    <span class="closebtn" onClick={() => setTagAlert(false)}>&times;</span>
                    {"User with tag " + tag + " already exists!"}
                </div> : <></>
            }

            <input type="password" required placeholder="Password" id="password" name="password" value={password} onChange={e => setPassword(e.target.value)}/>
            <input type="password" required placeholder="Verify Password" id="verify_password" name="verify_password" value={verify_password} onChange={e => setVerificationPassword(e.target.value)}/>
            
            <input type="checkbox" id="remember" defaultChecked={remember} onChange={() => setRemember(!remember)}/>
            <label htmlFor="remember">Remember Me</label>
            <input type="submit" name="Login"/>
            <ThirdParty/>
        </Form>

    </>
}
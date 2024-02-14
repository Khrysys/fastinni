import { useEffect, useState } from "react"
import Form from "../../../blocks/Form";
import ThirdParty from "./ThirdParty";
import { ajax } from "jquery";
import { getCookie } from "../../../general/cookies";

export function LoginForm() {
    const [tag, setTag] = useState("")
    const [password, setPassword] = useState("")
    const [remember, setRemember] = useState(true)
    const [headerData, setHeaderData] = useState("")
    
    function onSubmit() {
        ajax(
            location.origin + "/api/account/login/", 
            {
                method: "POST",
                headers: {
                    "X-CSRF-Token": getCookie("csrf")
                },
                data: {
                    'tag': tag,
                    'password': password,
                }
            }
        ).done(function(data) {
            console.log(data)
            if(remember) {
                setCookie(Object.keys(data)[0], data.value)
            }
        }).fail(function(error) {
            console.log(error)
        })
    }

    // This gets the CSRF header info for this form
    useEffect(() => {
        ajax(location.origin + "/api/account/login").done(function(response) {
            setHeaderData(response.data)
        }).fail(function(error) {
            console.log(error)
        })
    }, [])

    return <>
        <header>
            <a>
                <b>Login to Fastinni</b>
            </a>
        </header>
        <Form onSubmit={() => onSubmit()}>
            <input type="text" required={true} maxLength="Tag length cannot be longer than 64 characters." data-val-length-max="64" placeholder="Tag" id="tag" name="tag" value={tag} onChange={e => setTag(e.target.value)} />
            <input type="password" required placeholder="Password" id="password" name="password" value={password} onChange={e => setPassword(e.target.value)}/>
            <input type="checkbox" id="remember" defaultChecked={remember} onChange={() => setRemember(!remember)}/>
            <label htmlFor="remember">Remember Me</label>
            <input type="submit" name="Login"/>
            <ThirdParty/>
        </Form>
    </>
}
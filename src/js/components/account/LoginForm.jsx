import { useState } from "react"
import { Form } from "../blocks/Form"
import { ajax } from "jquery"
import { setCookie } from "../../cookies"

export function LoginForm() {
    const [tag, setTag] = useState("")
    const [password, setPassword] = useState("")
    const [remember, setRemember] = useState(true)

    function onSubmit() {
        ajax(
            process.env.NPM_API_URL + "account/login", 
            data={
                'tag': tag,
                'password': password,
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

    return <div className="login-form">
        <header>
            <a>
                <b>Login to Fastinni</b>
            </a>
        </header>
        <Form onSubmit={onSubmit}>
            <input type="text" required={true} maxLength="Tag length cannot be longer than 64 characters." data-val-length-max="64" placeholder="Tag" id="tag" name="tag" value={tag} onChange={e => setTag(e.target.value)} />
            <input type="password" required placeholder="Password" id="password" name="password" value={password} onChange={e => setPassword(e.target.value)}/>
            <input type="checkbox" id="remember" defaultChecked={remember} onChange={() => setRemember(!remember)}/>
            <label htmlFor="remember">Remember Me</label>
            <input type="submit" name="Login"/>
        </Form>
    </div>
}
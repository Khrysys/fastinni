import { useEffect } from "react";
import Form from "../../blocks/Form";
import ThirdParty from "./ThirdParty";
import { ajax } from "jquery";

export function SignupForm() {
    const [tag, setTag] = useState("")
    const [password, setPassword] = useState("")
    const [verify_password, setVerificationPassword] =useState("")
    const [remember, setRemember] = useState(true)
    const [headerData, setHeaderData] = useState("")
    const [tagAlert, setTagAlert] = useState(false);
    
    function onSubmit() {

    }

    function checkTagAvailibility(val) {
        ajax(location.origin + "/api/account/tag").done(function(response) {
            
        }.fail(function(error) {

        }))
    }

    // This gets the CSRF header info for this form
    useEffect(() => {
        ajax(location.origin + "/api/account/signup").done(function(response) {
            setHeaderData(response.data)
        }).fail(function(error) {
            console.log(error)
        })
    }, [])

    return <>
        <header>
            <a>
                <b>Create a New Account</b>
            </a>
        </header>
        <Form onSubmit={() => onSubmit()}>
            <input type="text" required={true} maxLength="Username length cannot be longer than 64 characters." data-val-length-max="64" placeholder="Username" id="username" name="username" value={username} onChange={e => setTag(e.target.value)} />
            <input type="text" required={true} maxLength="Tag length cannot be longer than 64 characters." data-val-length-max="64" placeholder="Tag" id="tag" name="tag" value={tag} onChange={e => {setTag(e.target.value);checkTagAvailibility(e.target.value)}} />
            {
                <div className="alert">
                <span class="closebtn" onclick={displayAlert(false)}>&times;</span>
                This is an alert box.
            </div>
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
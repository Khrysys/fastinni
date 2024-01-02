import { useEffect } from "react"

export default function LoginForm() {
    const [tag, setTag] = useState("")
    const [password, setPassword] = useState("")
    const [remember, setRemember] = useState(true)
    
    function onSubmit() {
        ajax(
            window.location.origin + "/api/latest/account/login/", 
            {
                method: "POST",
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
        ajax(window.location.origin + "/api/latest/account/login")
    })

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
            <div className="third-party">
                <p>Additional Sign-in Services</p>
                <div className="icons">
                    <a href={process.env.NPM_API_URL + "oauth/google/"}>
                        < FaSquareGooglePlus size={40}/>
                    </a>
                    <a href={process.env.NPM_API_URL + "oauth/github/"}>
                        < FaSquareGithub size={40} />
                    </a>
                    <a href={process.env.NPM_API_URL + "oauth/discord"}>
                        < BiLogoDiscord size={40}/>
                    </a>
                    <a href={process.env.NPM_API_URL + "oauth/twitter/"}>
                        < FaSquareXTwitter size={40} />
                    </a>
                    <a href={process.env.NPM_API_URL + "oauth/steam/"}>
                        < FaSquareSteam size={40} />
                    </a>
                </div>
            </div>
        </Form>
    </>
}
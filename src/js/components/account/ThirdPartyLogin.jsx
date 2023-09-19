import { FaGoogle, FaSquareGithub, FaSquareGooglePlus, FaSquareSteam, FaSquareXTwitter } from "react-icons/fa6"

const icoSize = 16

export function ThirdPartyLogin() {
    return <div className="third-party">
        <p>Additional Sign-in Services</p>
        <div className="icons">
            <a href={process.env.NPM_API_URL + "oauth/google"}>
                < FaSquareGooglePlus size={40}/>
            </a>
            <a href={process.env.NPM_API_URL + "oauth/github"}>
                < FaSquareGithub size={40} />
            </a>
            <a href={process.env.NPM_API_URL + "oauth/twitter"}>
                < FaSquareXTwitter size={40} />
            </a>
            <a href={process.env.NPM_API_URL + "oauth/steam"}>
                < FaSquareSteam size={40} />
            </a>
        </div>
        
    </div>
}
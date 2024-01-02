import { FaSquareGithub, FaSquareGooglePlus, FaSquareSteam, FaSquareXTwitter } from "react-icons/fa6";
import { BiLogoDiscord } from "react-icons/bi";

export default function ThirdParty() {
    return <div className="third-party">
        <p>Additional Sign-in Services</p>
        <div className="icons">
            <a href={"/api/latest/oauth/google/"}>
                < FaSquareGooglePlus size={40}/>
            </a>
            <a href={"/api/latest/oauth/github/"}>
                < FaSquareGithub size={40} />
            </a>
            <a href={"/api/latest/oauth/discord"}>
                < BiLogoDiscord size={40}/>
            </a>
            <a href={"/api/latest/oauth/twitter/"}>
                < FaSquareXTwitter size={40} />
            </a>
            <a href={"/api/latest/oauth/steam/"}>
                < FaSquareSteam size={40} />
            </a>
        </div>
    </div>
}
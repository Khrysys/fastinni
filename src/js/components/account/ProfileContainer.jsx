import { useContext } from "react"
import { UsernameContext } from "../../contexts/AccountContext"
import { Form } from "../blocks/Form"

export function ProfileContainer() {
    const username = useContext(UsernameContext)
    const tag = useContext(UsernameContext)
    const email = useContext(UsernameContext)
    const image = useContext(UsernameContext)
    const login = useContext(UsernameContext)

    return <div className="profile-container">
        <Form >
            <input type="text" required={true} maxLength="Tag length cannot be longer than 64 characters." data-val-length-max="64" placeholder="Tag" id="tag" name="tag" value={tag} onChange={e => setTag(e.target.value)} />
        </Form>
    </div>
}
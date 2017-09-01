export default function ({store, redirect}) {
  if (store.state.auth_token === null) {
    return redirect('/login?next=')
  }
}

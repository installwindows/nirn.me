# nirn.me

Your Firefox new tab. The webpage that was missing.

## But why ?

/ -> VIP users can create and manage slugs with an optional passphrase

/{slug} -> After inputing the passphrase, the user has access to a canvas (not the html element)
where you can:
- Create/Manage "Nirn"
- Sync the Nirnroot to your computer/termux


## Nirnroot

Host the nirns.

## Nirn

Text, links, files.

## Build and install

Follow the instructions.

Make migrations:
`django-admin makemigrations nirn --pythonpath=. --settings=settings`

Mirate:
`django-admin migrate nirn 0 --pythonpath=. --settings=settings`

Run dev server:
`django-admin runserver --pythonpath=. --settings=settings`

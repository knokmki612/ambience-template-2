TEMPLATE = aux
NAME=template
OTHER_FILES = \
        $${NAME}.ambience \
        sounds.index \
        images/* \
        sounds/* \
        translations/* \
        rpm/* \
        README

ambience.files = \
        $${NAME}.ambience \
        sounds.index
ambience.path = /usr/share/ambience/$${NAME}

images.files = images/*
images.path = $${ambience.path}/images

sounds.files = sounds/*
sounds.path = $${ambience.path}/sounds

INSTALLS += \
        ambience \
        images \
        sounds

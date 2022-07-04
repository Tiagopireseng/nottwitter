import React from "react";

import Feed from "../Feed";

import {
    Container,
    Banner,
    Avatar,
    ProfileData,
    LocationIcon,
    CakeIcon,
    Followage,
    EditButton,
} from "./styles";

const HomePage: React.FC = () => {
    return (
        <>
            <Container>
                <Banner>
                    <img src={require("./images/wallpaper.jpg")} alt="" />
                    <Avatar>
                        <img
                            src="	https://avatars.githubusercontent.com/u/89080061?v=4"
                            alt="Avatar"
                        />
                    </Avatar>
                </Banner>

                <ProfileData>
                    <EditButton outlined>Editar perfil</EditButton>

                    <h1>Tiago Pires</h1>
                    <h2>@tiagopiresss</h2>

                    <p>
                        Developer at Ford
                        <a href="https://github.com/Tiagopireseng">
                            @Ford-Motor
                        </a>
                    </p>

                    <ul>
                        <li>
                            <LocationIcon />
                            Natal, Brasil
                        </li>
                        <li>
                            <CakeIcon />
                            Nascido(a) em 20 de Abril de 1994
                        </li>
                    </ul>

                    <Followage>
                        <span>
                            seguindo <strong>912</strong>
                        </span>
                        <span>
                            <strong>327 </strong> seguidores
                        </span>
                    </Followage>
                </ProfileData>

                <Feed />
            </Container>
        </>
    );
};

export default HomePage;

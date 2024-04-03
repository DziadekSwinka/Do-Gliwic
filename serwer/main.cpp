#include <SFML/Network.hpp>
#include <SFML/Graphics.hpp>
#include <iostream>
#include "json.hpp"

int main() {
    using json = nlohmann::json;
    sf::UdpSocket socket;
    if (socket.bind(1313) != sf::Socket::Done) {
        std::cerr << "Blad podczas wiazania gniazda z portem 1313." << std::endl;
        return 1;
    }
    sf::IpAddress senderIp;
    unsigned short senderPort;
    const int datasize = 1024;
    char data[datasize] = {0};
    std::size_t received;

    sf::RenderWindow window(sf::VideoMode(800, 600), "Serwer");
    std::cout<<"Serwer"<<std::endl;
    sf::Text CurrentTemp, CurrentHum;
    sf::Font font;
    font.loadFromFile("arial.ttf");
    CurrentTemp.setCharacterSize(24);
    CurrentTemp.setFont(font);
    CurrentTemp.setFillColor(sf::Color::Red);
    CurrentHum.setCharacterSize(24);
    CurrentHum.setFont(font);
    CurrentHum.setFillColor(sf::Color::Red);
    CurrentHum.move(0,50);
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }
        if (socket.receive(data, datasize, received, senderIp, senderPort) != sf::Socket::Done) {
        continue;
        }
        try {
        json parsed_data = json::parse(data);
            std::cout<<parsed_data<<std::endl<<parsed_data["hum"]<<std::endl;
            std::string t=parsed_data["temp"];
            std::string h=parsed_data["hum"];
            CurrentTemp.setString(t);
            CurrentHum.setString(h);
            window.clear(sf::Color::White);
            window.draw(CurrentTemp);
            window.draw(CurrentHum);
            window.display();
        } catch (const json::parse_error& e)
        {
            std::cerr << "JSON parse error: " << e.what() << " at byte " << e.byte << std::endl;
        }



    }
    return 0;


}

#include <SFML/Network.hpp>
#include <SFML/Graphics.hpp>
#include <iostream>

int main() {
    sf::UdpSocket socket;
    if (socket.bind(1313) != sf::Socket::Done) {
        std::cerr << "B³¹d podczas wi¹zania gniazda z portem 1313." << std::endl;
        return 1;
    }
    sf::IpAddress senderIp;
    unsigned short senderPort;
    const int datasize = 4;
    char data[datasize] = {0};
    std::size_t received;
    sf::RenderWindow window(sf::VideoMode(800, 600), "Serwer");
    sf::Text CurrentTemp;
    sf::Font font;
    font.loadFromFile("arial.ttf");
    CurrentTemp.setCharacterSize(24);
    CurrentTemp.setFont(font);
    CurrentTemp.setFillColor(sf::Color::Red);
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
        CurrentTemp.setString(data);
        window.clear(sf::Color::White);
        window.draw(CurrentTemp);
        window.display();


    }
    return 0;


}

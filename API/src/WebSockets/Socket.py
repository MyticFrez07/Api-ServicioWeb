from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room
from src.Database.database import app

socketio = SocketIO(app, cors_allowed_origins="*")

# Almacena los eventos de dibujo en el servidor
drawing_events = []

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado al servidor Socket.IO')
    # Unirse a la sala única para todos los sockets
    join_room('draw_room')

    # Enviar todos los eventos de dibujo almacenados al cliente que se conectó
    emit('draw_events', drawing_events, room='draw_room')

@socketio.on('draw_event')
def handle_draw_event(data):
    # Almacenar el evento de dibujo en la lista
    drawing_events.append(data)

    # Reenviar el evento a todos los clientes conectados en la misma sala, incluyendo el emisor
    emit('draw_event', data, room='draw_room', include_self=True)

@socketio.on('clear_canvas')
def handle_clear_canvas():
    # Borrar la lista de eventos de dibujo almacenados
    drawing_events.clear()

    # Emitir un evento "clear_canvas" a todos los clientes conectados en la misma sala
    emit('clear_canvas', room='draw_room', include_self=True)



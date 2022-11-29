from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
import valve.source
import valve.source.a2s
import re
import paramiko

# Create your views here.
from .models import *
from .forms import *


class ServerListView(ListView):
    model = Server
    queryset = Server.objects.order_by('-host')


class ServerDetailView(DetailView):
    model = Server
    slug_field = "slug"

    # def StartServer(self, pk):
    #     server = Server.objects.get(id=pk)
    #     client = paramiko.SSHClient()
    #     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     client.connect(hostname=server.model.host, username=server.model.server_username, password=server.model.secret,
    #                    port=server.model.port)
    #     stdin, stdout, stderr = client.exec_command('./csgoserver start')
    #     data = stdout.read() + stderr.read()
    #     client.close()
    #
    # def StopServer(self, pk):
    #     server = Server.objects.get(id=pk)
    #     client = paramiko.SSHClient()
    #     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     client.connect(hostname=server.model.host, username=server.model.server_username, password=server.model.secret,
    #                    port=server.model.port)
    #     stdin, stdout, stderr = client.exec_command('./csgoserver stop')
    #     data = stdout.read() + stderr.read()
    #     client.close()
    #
    # def DetailsServer(self, pk):
    #     server = Server.objects.get(id=pk)
    #     client = paramiko.SSHClient()
    #     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     client.connect(hostname=server.model.host, username=server.model.server_username, password=server.model.secret,
    #                    port=server.model.port)
    #     stdin, stdout, stderr = client.exec_command('./csgoserver detail')
    #     data = stdout.read() + stderr.read()
    #     client.close()
    #
    # def DebugServer(self, pk):
    #     server = Server.objects.get(id=pk)
    #     client = paramiko.SSHClient()
    #     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     client.connect(hostname=server.model.host, username=server.model.server_username, password=server.model.secret,
    #                    port=server.model.port)
    #     stdin, stdout, stderr = client.exec_command('./csgoserver debug')
    #     data = stdout.read() + stderr.read()
    #     client.close()


class AddServer(Server, View):

    def get(self, request, *args, **kwargs):
        form = AddServerForm(request.POST or None)
        servers = Server.objects.all()
        context = {'form': form, 'csservers': servers}
        return render(request, 'csservers/server_add.html', context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        error = ''
        if request.method == "POST":
            form = AddServerForm(request.POST or None)
            form.user = request.user
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.save()
                return redirect('/servers/')
            else:
                error = form.errors
        form = AddServerForm()
        context = {
            'form': form,
            'error': error,
        }
        return render(request, 'csservers/server_add.html', context)


class StartServer(Server, View):

    def get(self, request, *args, **kwargs):
        form = AddServerForm(request.POST or None)
        servers = Server.objects.all()
        context = {'form': form, 'csservers': servers}
        return render(request, 'csservers/server_detail.html', context)

    # def post(self, request, *args, **kwargs):
    #     pass

    # def start_server(self, request, pk):
    #     print(request.POST)
    #     if request.POST:
    #         form = StartServerForm(request.POST or None)
    #         server = Server.objects.get(id=pk)
    #         if form.is_valid():
    #             new_from = form.save(commit=False)
    #             new_from.host = server.host
    #             new_from.server_username = server.server_username
    #             new_from.secret = server.secret
    #             new_from.port = server.ssh_port
    #             new_from.save()
    #             client = paramiko.SSHClient()
    #             client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #             client.connect(hostname=new_from.host, username=new_from.server_username, password=new_from.secret,
    #                            port=new_from.port)
    #             stdin, stdout, stderr = client.exec_command('./csgoserver sp')
    #             data = stdout.read() + stderr.read()
    #             client.close()
    #             return redirect('servers/<slug:slug>/start_server/<int:id>')

    def post(self, request, pk):
        print(f'POST: {request.POST}')
        print(f'GET: {request.GET}')
        server = Server.objects.get(id=pk)
        if request.POST:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=server.host, username=server.server_username, password=server.secret,
                           port=server.ssh_port)
            stdin, stdout, stderr = client.exec_command('./csgoserver st')
            data = stdout.read() + stderr.read()
            client.close()
            return redirect(server.get_absolute_url())
        return redirect(server.get_absolute_url())


class StopServer(Server, View):

    def get(self, request, *args, **kwargs):
        form = AddServerForm(request.POST or None)
        servers = Server.objects.all()
        context = {'form': form, 'csservers': servers}
        return render(request, 'csservers/server_detail.html', context)

    def post(self, request, pk):
        print(f'POST: {request.POST}')
        print(f'GET: {request.GET}')
        server = Server.objects.get(id=pk)
        if request.POST:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=server.host, username=server.server_username, password=server.secret,
                           port=server.ssh_port)
            stdin, stdout, stderr = client.exec_command('./csgoserver sp')
            data = stdout.read() + stderr.read()
            client.close()
            return redirect(server.get_absolute_url())
        return redirect(server.get_absolute_url())


# class ReloadServer(Server, View):
#
#     def get(self, request, *args, **kwargs):
#         pass
#
#     def post(self, request, *args, **kwargs):
#         pass
#
#
# class DebugServer(Server, View):
#
#     def get(self, request, *args, **kwargs):
#         pass
#
#     def post(self, request, *args, **kwargs):
#         pass
#
#
# class DetailsServer(Server, View):
#
#     def get(self, request, *args, **kwargs):
#         pass
#
#     def post(self, request, *args, **kwargs):
#         pass

class TakeMap(Server, View):

    def get(self, request, *args, **kwargs):
        form = AddServerForm(request.POST or None)
        servers = Server.objects.all()
        context = {'form': form, 'csservers': servers}
        return render(request, 'csservers/server_detail.html', context)

    def post(self, request, pk):
        print(f'POST: {request.POST}')
        print(f'GET: {request.GET}')
        server = Server.objects.get(id=pk)
        requested_html = re.search(r'^text/html', request.META.get('HTTP_ACCEPT'))
        if not requested_html:
            server_address = (server.host, server.server_port)
            try:
                with valve.source.a2s.ServerQuerier(server_address) as cs_server:
                    info = cs_server.info()
                    players = cs_server.players()

                    cs_server_name = "{server_name}".format(**info)
                    max_players = "{max_players}".format(**info)
                    players_on_server = "{player_count}".format(**info)
                    server_map = "{map}".format(**info)


                    print("{player_count}/{max_players} {server_name}".format(**info))
                    for player in sorted(players["players"],
                                         key=lambda p: p["score"], reverse=True):
                        print("{score} {name}".format(**player))

                    Server.objects.update(server_name=cs_server_name)
                    Server.objects.update(player_count=players_on_server)
                    Server.objects.update(max_players=max_players)
                    Server.objects.update(map=server_map)
                    return redirect(server.get_absolute_url())

            except valve.source.NoResponseError:
                print("Server {}:{} timed out!".format(*server_address))
        else:
            print("-------------YA EBAL-------------")
            return redirect(server.get_absolute_url())
        return redirect(server.get_absolute_url())

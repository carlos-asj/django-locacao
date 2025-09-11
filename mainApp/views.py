from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import veiculo
from .forms import VeiculoForm

from .models import modelo

def index(request):
    return render(request, "index.html",)

# Criar uma nova tarefa
class AddVeiculo(CreateView):
    model = veiculo
    form_class = VeiculoForm
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('task_list')
    
    def form_valid(self, form):
        # Você pode adicionar lógica adicional aqui antes de salvar
        return super().form_valid(form)

# Editar uma tarefa existente
class UpdateVeiculo(UpdateView):
    model = veiculo
    form_class = VeiculoForm
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('task_list')

# Excluir uma tarefa
class DeleteVeiculo(DeleteView):
    model = veiculo
    template_name = 'veiculo_confirm_delete.html'
    success_url = reverse_lazy('task_list')

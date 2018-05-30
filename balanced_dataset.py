import torch


def get_balanced_indices(label_vector, samples_per_class):
    n_classes = torch.unique(label_vector).numel()
    indices_per_class = []
    for i in range(n_classes):
        indices_per_class.append(torch.nonzero(label_vector == i)[:samples_per_class])
    return torch.cat(indices_per_class).squeeze()


if __name__ == '__main__':
    from torchvision.datasets import MNIST
    import torchvision.transforms as transforms
    from torch.utils.data import DataLoader
    from torch.utils.data.sampler import SubsetRandomSampler

    train_transforms = transforms.Compose([transforms.ToTensor(),
                                           transforms.Normalize((0.1307,), (0.3081,))
                                           ])
    train_data = MNIST('~/MNIST', train=True, transform=train_transforms, download=True)

    samples_per_class_per_epoch = [1, 2, 4, 8, 16]
    n_classes = 10

    epochs = 5
    batch_size = 32
    for i in range(epochs):
        # get a list of indices which have the same number of examples for each class
        # if you request 1 you will have one sample for each label [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # if you then request 2, you will have the same samples as before, but now 10 new ones - one more for each label
        indices = get_balanced_indices(train_data.train_labels, samples_per_class_per_epoch[i])
        # print(indices)
        # if the batch_size is bigger than the number of samples, use the number of samples as batch size
        if samples_per_class_per_epoch[i]*n_classes < batch_size:
            effective_batch_size = samples_per_class_per_epoch[i]*n_classes
        else:
            effective_batch_size = batch_size

        # dataloader instantiation is cheap
        dataloader = torch.utils.data.DataLoader(train_data, batch_size=effective_batch_size,
                                                 sampler=SubsetRandomSampler(indices))
        sum_check = 0
        for image, target in dataloader:
            sum_check += target.sum()

        print(sum_check==45*samples_per_class_per_epoch[i])


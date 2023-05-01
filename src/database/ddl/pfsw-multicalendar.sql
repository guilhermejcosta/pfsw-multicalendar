CREATE TABLE `calendar` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `owner_id` int,
  `organization_id` int,
  `title` varchar(255),
  `description` varchar(255),
  `created_at` timestamp,
  `deleted_at` timestamp,
  `updated_at` timestamp,
  `shared` boolean
);

CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255),
  `display_name` varchar(255),
  `email` varchar(255),
  `contact_phone` integer,
  `created_at` timestamp,
  `deleted_at` timestamp,
  `updated_at` timestamp
);

CREATE TABLE `organization` (
  `owner_id` int,
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `created_at` timestamp,
  `updated_at` timestamp,
  `deleted_at` timestamp
);

CREATE TABLE `organization_users` (
  `organization_id` int PRIMARY KEY,
  `user_id` varchar(255),
  `type_user` int
);

CREATE TABLE `type_user_organization` (
  `id` int PRIMARY KEY,
  `description` varchar(255)
);

ALTER TABLE `calendar` ADD FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`);

ALTER TABLE `calendar` ADD FOREIGN KEY (`organization_id`) REFERENCES `organization` (`id`);

ALTER TABLE `organization` ADD FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`);

ALTER TABLE `organization_users` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `organization_users` ADD FOREIGN KEY (`type_user`) REFERENCES `type_user_organization` (`id`);

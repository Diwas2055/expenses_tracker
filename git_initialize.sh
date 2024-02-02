#!/bin/bash

function git_initialize(){
    # Prompt user for the project path
    read -p "Enter project path: " project_path

    # Set default path to current directory if empty
    project_path="${project_path:-.}"
    
    # Display the project path
    echo "Project path: $project_path"

    # Check if the directory exists
    if [ -e "$project_path" ]; then
        # Check if it's already a Git repository
        if [ -d "$project_path/.git" ]; then
            echo "Git repository already exists in this directory."
        else
            echo "Directory already exists, but it is not a Git repository."
            read -p "Would you like to initialize a Git repository in this directory? (y/n) " initialize
            if [ "$initialize" == "y" ]; then
                cd $project_path
                git init
                echo "Git repository initialized."
            else
                echo "Git repository not initialized."
                exit 1
            fi
        fi
    fi
}

function remote_origin(){
    remote_name="origin"
    cd $project_path
    git_url=$(git remote get-url $remote_name 2>/dev/null)
    if [ -z "$git_url" ]; then
        echo "Remote '$remote_name' does not exist."
        # Prompt user for the remote repository URL
        read -p "Enter remote repository URL: " remote_url
        # Add the remote repository
        git remote add origin $remote_url
        echo "Remote repository added."
    else
        echo "Remote '$remote_name' URL: $git_url"
        read -p "Would you like to change the remote URL? (y/n) " change_url
        if [ "$change_url" == "y" ]; then
            read -p "Enter new remote repository URL: " new_remote_url
            git remote set-url $remote_name $new_remote_url
            echo "Remote URL updated."
            read -p "Would yo like to create a new branch? (y/n) " new_branch
            if [ "$new_branch" == "y" ]; then
                read -p "Enter branch name: " branch_name
                git checkout -b $branch_name
                echo "New branch created."
            else
                echo "No new branch created."
                git branch --m master
                echo "Current branches: master"
            fi
        else
            echo "Remote URL not updated."
        fi
    fi
}

function add_commit_push(){
    cd $project_path

    # Add all files to the staging area
    git add .

    # Commit the changes
    read -p "Enter commit message: " commit_message
    git commit -m "$commit_message"

    # Push the changes to the remote repository
    echo "Where to push?"
    read -i "$current" -e branch

    echo "You sure you wanna push? (y/n)"
    read -i "y" -e yn

    if [ "$yn" == "y" ]; then
        git push origin $branch
    else
        echo "Changes not pushed."
    fi
}


git_initialize
remote_origin
add_commit_push

exit 1
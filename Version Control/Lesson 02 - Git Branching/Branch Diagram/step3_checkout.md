# Step 3: git checkout main

Switch back to the main branch to prepare for merging.

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Main commit 1"
    commit id: "Main commit 2" type: HIGHLIGHT
    branch feature-a
    checkout feature-a
    commit id: "Feature commit 1'"
    commit id: "Feature commit 2'"
    commit id: "Feature commit 3'"
```

**What happened?**
- `git checkout main` switched your working directory to the main branch
- You're now positioned at the tip of main
- Ready to bring in the changes from feature-a

**Next Step:**
- Now you can merge the feature branch into main

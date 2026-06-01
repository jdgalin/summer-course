# Step 2: git rebase main

Replay your feature commits on top of the updated main branch.

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Main commit 1"
    commit id: "Main commit 2"
    branch feature-a
    checkout feature-a
    commit id: "Feature commit 1'"
    commit id: "Feature commit 2'"
    commit id: "Feature commit 3'" type: HIGHLIGHT
```

**What happened?**
- `git rebase main` moved your feature commits to start from the tip of main
- Your commits got new identifiers (notice the `'` marks) because they were rewritten
- This creates a linear history without merge commits
- Your feature branch now includes all the latest changes from main

**Important Notes:**
- Rebasing rewrites commit history
- Never rebase commits that have been pushed to a shared branch
- Perfect for cleaning up local development before merging

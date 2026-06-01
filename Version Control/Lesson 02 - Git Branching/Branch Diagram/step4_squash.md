# Step 4: git merge --squash feature-a

Squash all feature commits into a single set of changes.

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Main commit 1"
    commit id: "Main commit 2"
    branch feature-a
    checkout feature-a
    commit id: "Feature commit 1'"
    commit id: "Feature commit 2'"
    commit id: "Feature commit 3'"
    checkout main
    commit id: "Staging squashed changes" type: REVERSE
```

**What happened?**
- `git merge --squash feature-a` takes all changes from feature-a
- Combines them into a single set of staged changes
- Does NOT create a commit yet
- Does NOT preserve the individual commit history from feature-a

**What's in staging?**
- All the file changes from Feature commit 1', 2', and 3'
- Ready to be committed as one clean commit

**Benefits:**
- Clean main branch history
- One commit per feature
- Easy to revert entire features
- Easier to review the full feature changes

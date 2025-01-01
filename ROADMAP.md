
- Never work directly on `main`
- Create new features on branches:
  ```bash
  git checkout -b feature/risk-control-agent
  ```

### 2. Development Process
1. Start each feature:
   ```bash
   git checkout develop
   git pull
   git checkout -b feature/new-feature
   ```

2. Work on your code
3. Commit regularly:
   ```bash
   git add .
   git commit -m "✨ Added new risk control feature"
   ```

4. Push feature:
   ```bash
   git push origin feature/new-feature
   ```

5. Create Pull Request on GitHub to merge into `develop`

## 🎯 Best Practices

### Code Organization
1. Keep modules small and focused
2. Use clear naming conventions
3. Document with docstrings
4. Add print statements for debugging:
   ```python
   print(f"🌙 Moon Dev Debug: Processing trade signal: {signal}")
   ```

### Git Commits
- Use emoji prefixes:
  - ✨ New feature
  - 🐛 Bug fix
  - 📚 Documentation
  - ⚡️ Performance
  - 🧪 Tests

### Testing
1. Write tests for new features
2. Run tests before commits
3. Use pytest for testing

## 📝 Development Steps

1. **Setup Phase**
   - [x] Initialize repository
   - [x] Create README
   - [ ] Set up project structure
   - [ ] Create requirements.txt

2. **Core Development**
   - [ ] Build risk control agent
   - [ ] Develop exit strategy agent
   - [ ] Create entry agent
   - [ ] Implement sentiment analysis
   - [ ] Design strategy execution

3. **Testing & Documentation**
   - [ ] Write unit tests
   - [ ] Create usage examples
   - [ ] Document API
   - [ ] Add installation guide

## 🔑 Remember
- Commit often
- Use clear commit messages
- Test before pushing
- Document as you go
- Keep security in mind (no API keys!)
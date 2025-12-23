# Contributing to Chocolate Mint Gelato Recipe

First off, thank you for considering contributing to this recipe repository! 🍦

## How Can I Contribute?

### Reporting Issues

If you've tried the recipe and encountered problems, please open an issue with:

- **What went wrong:** Describe the issue (texture, flavor, technique problem)
- **What you did:** Your exact steps and measurements
- **Your setup:** Type of ice cream maker, ingredient brands, environment (altitude, humidity)
- **Photos:** If possible, include photos of the result

### Suggesting Improvements

Have an idea to make this recipe better? We'd love to hear it!

**Before suggesting:**
- Check if the suggestion has already been made
- Make sure it aligns with authentic gelato principles
- Test the modification if possible

**When suggesting:**
- Explain the reasoning behind your suggestion
- Provide scientific basis if applicable
- Share test results if you've tried it

### Recipe Variations

Want to share a variation? Great! Consider:

- **Mint variations:** Different mint types (peppermint, spearmint, chocolate mint)
- **Chocolate variations:** Different chocolate percentages, white chocolate
- **Alternative ingredients:** Dairy-free, sugar-free, egg-free versions
- **Flavor combinations:** Other complementary flavors

Submit variations as separate documentation or in a `VARIATIONS.md` file.

### Code Contributions

Contributing to `gelato_maker.py`? Please:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/your-feature-name`
3. **Follow Python style guidelines:**
   - PEP 8 style guide
   - Type hints where appropriate
   - Docstrings for functions and classes
4. **Test your changes:** Make sure the script runs without errors
5. **Commit with clear messages:** Describe what and why
6. **Submit a pull request**

#### Code Style

```python
def calculate_ingredient(amount: float, scale: float) -> float:
    """
    Calculate scaled ingredient amount.
    
    Args:
        amount: Original ingredient amount
        scale: Scale factor
        
    Returns:
        Scaled amount
    """
    return amount * scale
```

### Documentation Improvements

Documentation can always be better! Contributions welcome for:

- **Clarity:** Making instructions clearer
- **Detail:** Adding helpful details from experience
- **Corrections:** Fixing typos or inaccuracies
- **Translations:** Translating to other languages
- **Photos/Videos:** Visual guides for steps

### Testing

If you make the gelato, please share your results:

1. Use the Python script to log your batch
2. Note any deviations from the recipe
3. Share your rating and feedback
4. Include photos if possible

## Pull Request Process

1. **Update documentation** if you've changed functionality
2. **Update the README.md** if you've added features
3. **Add your changes to CHANGELOG.md** (if we have one)
4. **Test thoroughly** before submitting
5. **Link any related issues** in your PR description

## Recipe Testing Guidelines

When testing recipe modifications:

### Document Everything
- Exact ingredients (brands, fat percentages)
- Equipment used
- Ambient temperature and humidity
- Timing for each step
- Final temperature readings

### Control Variables
- Change only ONE variable at a time
- Make the original recipe first as a control
- Use the same equipment and technique

### Evaluate Results
- **Texture:** Smooth? Icy? Dense? Creamy?
- **Flavor:** Balanced? Too sweet? Mint strength?
- **Appearance:** Color, shine, consistency
- **Scoopability:** How hard/soft when serving?
- **Melting:** How does it melt? Clean or separated?

### Scientific Approach
- Use a thermometer
- Weigh ingredients (don't use volume for precision)
- Take notes in real-time
- Rate on consistent scale (1-5 stars)

## Style Guide

### Documentation Style

- **Be clear and concise**
- **Use active voice:** "Add the sugar" not "The sugar should be added"
- **Include measurements:** Both metric and imperial
- **Explain the why:** Help people understand the science
- **Be encouraging:** Gelato making should be fun!

### Formatting

- Use markdown formatting consistently
- Use bullet points for lists
- Use numbered lists for sequential steps
- Include emojis sparingly for visual interest
- Use tables for comparisons

### Temperature Conventions

Always include both Celsius and Fahrenheit:
- Format: `82-84°C (180-183°F)`
- Celsius first, Fahrenheit in parentheses

### Measurement Conventions

- **Prefer weight over volume** for precision
- **Metric first:** `150g (5.3 oz)`
- For small amounts: `1/4 tsp (1.25 ml)`

## Community Guidelines

### Be Respectful
- Respect different skill levels
- Be constructive with criticism
- Assume good intentions

### Be Helpful
- Answer questions when you can
- Share your experiences
- Encourage experimentation

### Be Scientific
- Back up claims with evidence
- Cite sources
- Admit when you're unsure

## Questions?

Don't hesitate to ask questions! Open an issue labeled "question" and we'll help out.

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Special thanks in documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Happy gelato making! 🍦🌿🍫**


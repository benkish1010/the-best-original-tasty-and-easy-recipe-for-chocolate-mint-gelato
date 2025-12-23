#!/usr/bin/env python3
"""
Chocolate Mint Gelato Maker - Interactive Recipe Assistant
==========================================================

This script helps you make perfect chocolate mint gelato by:
- Guiding you through each step
- Tracking temperatures and timing
- Scaling ingredients
- Logging your batches for future reference

Author: Gelato Enthusiasts
License: MIT
"""

import time
import json
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class Step(Enum):
    """Gelato making steps"""
    MINT_INFUSION = 1
    CHOCOLATE_MELTING = 2
    CUSTARD_COOKING = 3
    CHILLING = 4
    CHURNING = 5
    FREEZING = 6
    COMPLETE = 7


@dataclass
class Ingredient:
    """Represents a recipe ingredient"""
    name: str
    amount: float
    unit: str
    notes: str = ""
    
    def scale(self, factor: float) -> 'Ingredient':
        """Scale ingredient amount by factor"""
        return Ingredient(
            name=self.name,
            amount=self.amount * factor,
            unit=self.unit,
            notes=self.notes
        )
    
    def __str__(self) -> str:
        note_str = f" ({self.notes})" if self.notes else ""
        return f"{self.amount:.1f}{self.unit} {self.name}{note_str}"


@dataclass
class Recipe:
    """Complete gelato recipe"""
    name: str
    yield_amount: str
    base_ingredients: List[Ingredient]
    chocolate_ingredients: List[Ingredient]
    optional_ingredients: List[Ingredient]
    
    def scale(self, factor: float) -> 'Recipe':
        """Scale entire recipe by factor"""
        return Recipe(
            name=self.name,
            yield_amount=f"{factor:.1f}x original ({self.yield_amount})",
            base_ingredients=[ing.scale(factor) for ing in self.base_ingredients],
            chocolate_ingredients=[ing.scale(factor) for ing in self.chocolate_ingredients],
            optional_ingredients=[ing.scale(factor) for ing in self.optional_ingredients]
        )
    
    def display(self):
        """Display recipe in readable format"""
        print(f"\n{'='*60}")
        print(f"  🍦 {self.name}")
        print(f"{'='*60}")
        print(f"Yield: {self.yield_amount}\n")
        
        print("BASE INGREDIENTS:")
        for ing in self.base_ingredients:
            print(f"  • {ing}")
        
        print("\nCHOCOLATE COMPONENTS:")
        for ing in self.chocolate_ingredients:
            print(f"  • {ing}")
        
        if self.optional_ingredients:
            print("\nOPTIONAL:")
            for ing in self.optional_ingredients:
                print(f"  • {ing}")
        print()


@dataclass
class BatchLog:
    """Log of a gelato batch"""
    timestamp: str
    scale_factor: float
    mint_steep_time: int
    custard_final_temp: float
    chill_hours: float
    churn_minutes: int
    notes: str
    rating: Optional[int] = None


class GelatoMaker:
    """Interactive gelato making assistant"""
    
    def __init__(self):
        self.recipe = self._create_default_recipe()
        self.current_step = Step.MINT_INFUSION
        self.batch_log = None
        self.scale_factor = 1.0
        
    def _create_default_recipe(self) -> Recipe:
        """Create the default chocolate mint gelato recipe"""
        base = [
            Ingredient("whole milk", 600, "g", "3.25% fat"),
            Ingredient("heavy cream", 200, "g", "35%+ fat"),
            Ingredient("granulated sugar", 150, "g"),
            Ingredient("large egg yolks", 4, " ", "about 75-85g"),
            Ingredient("fresh mint leaves", 30, "g", "stems removed, washed"),
            Ingredient("fine salt", 0.25, "tsp"),
        ]
        
        chocolate = [
            Ingredient("unsweetened cocoa powder", 40, "g", "Dutch-process preferred"),
            Ingredient("dark chocolate", 100, "g", "60-70% cacao, chopped"),
        ]
        
        optional = [
            Ingredient("mini chocolate chips", 50, "g", "for stracciatella effect"),
        ]
        
        return Recipe(
            name="Chocolate Mint Gelato",
            yield_amount="1 quart / 1 liter",
            base_ingredients=base,
            chocolate_ingredients=chocolate,
            optional_ingredients=optional
        )
    
    def run(self):
        """Run the interactive gelato maker"""
        print("\n" + "🍦" * 30)
        print("  CHOCOLATE MINT GELATO MAKER")
        print("🍦" * 30 + "\n")
        
        # Ask about scaling
        self._handle_scaling()
        
        # Display recipe
        self.recipe.display()
        
        input("Press Enter when you're ready to start making gelato...")
        
        # Initialize batch log
        self.batch_log = {
            'timestamp': datetime.now().isoformat(),
            'scale_factor': self.scale_factor,
            'mint_steep_time': 0,
            'custard_final_temp': 0,
            'chill_hours': 0,
            'churn_minutes': 0,
            'notes': '',
            'rating': None
        }
        
        # Execute steps
        self._step1_mint_infusion()
        self._step2_chocolate_melting()
        self._step3_custard_cooking()
        self._step4_chilling()
        self._step5_churning()
        self._step6_freezing()
        self._complete()
    
    def _handle_scaling(self):
        """Ask user if they want to scale the recipe"""
        print("Do you want to scale the recipe?")
        print("  1 = Full batch (1 quart)")
        print("  0.5 = Half batch")
        print("  2 = Double batch")
        
        while True:
            try:
                scale_input = input("Enter scale factor (default 1): ").strip()
                if not scale_input:
                    scale_input = "1"
                self.scale_factor = float(scale_input)
                if self.scale_factor > 0:
                    if self.scale_factor != 1:
                        self.recipe = self.recipe.scale(self.scale_factor)
                    break
                else:
                    print("Scale factor must be positive!")
            except ValueError:
                print("Please enter a valid number!")
    
    def _step1_mint_infusion(self):
        """Step 1: Mint infusion"""
        print("\n" + "="*60)
        print("STEP 1: MINT INFUSION (10-15 minutes)")
        print("="*60)
        
        print("\nInstructions:")
        print("1. Combine milk, cream, and mint leaves in heavy-bottom pot")
        print("2. Heat on medium until steaming (75-80°C / 167-176°F)")
        print("3. DO NOT BOIL")
        print("4. Remove from heat and cover")
        
        input("\nPress Enter when mixture is steaming and covered...")
        
        print("\n⏱️  Steeping for 10 minutes...")
        print("(In real cooking, wait 10 minutes. For demo, press Enter to continue)")
        input()
        
        while True:
            mint_strength = input("\nTaste the mint flavor. Is it strong enough? (y/n): ").lower()
            if mint_strength == 'y':
                self.batch_log['mint_steep_time'] = 10
                break
            elif mint_strength == 'n':
                print("Steep 5 more minutes...")
                input("Press Enter when done...")
                self.batch_log['mint_steep_time'] = 15
                break
        
        print("\n5. Strain out mint leaves using fine-mesh strainer")
        print("6. Press gently (don't crush or it becomes grassy)")
        
        input("\nPress Enter when mint is strained out...")
        print("✅ Step 1 complete!")
    
    def _step2_chocolate_melting(self):
        """Step 2: Add cocoa and melt chocolate"""
        print("\n" + "="*60)
        print("STEP 2: ADD COCOA + MELT CHOCOLATE (5 minutes)")
        print("="*60)
        
        print("\nInstructions:")
        print("1. While mixture is warm, whisk in:")
        print("   • Sugar")
        print("   • Cocoa powder")
        print("   • Salt")
        print("2. Whisk until no cocoa lumps remain")
        print("3. Add chopped dark chocolate")
        print("4. Stir until completely melted (60-70°C / 140-158°F)")
        
        input("\nPress Enter when chocolate is fully melted...")
        print("✅ Step 2 complete!")
    
    def _step3_custard_cooking(self):
        """Step 3: Temper eggs and cook custard"""
        print("\n" + "="*60)
        print("STEP 3: TEMPER EGGS + COOK CUSTARD (8-12 minutes)")
        print("="*60)
        
        print("\n⚠️  CRITICAL STEP - Must temper eggs properly!")
        print("\nInstructions:")
        print("1. In separate bowl, whisk egg yolks")
        print("2. TEMPER THE EGGS:")
        print("   • Ladle 1/4 cup hot mixture into eggs while whisking")
        print("   • Add another 1/4 cup, whisking constantly")
        print("   • Add one more 1/4 cup")
        
        input("\nPress Enter when eggs are tempered...")
        
        print("\n3. Pour tempered egg mixture back into pot")
        print("4. Cook on MEDIUM-LOW, stirring constantly")
        print("5. Target temperature: 82-84°C (180-183°F)")
        print("   • Should coat back of spoon")
        print("   • Draw finger through coating - line should remain")
        print("   • ⚠️ DO NOT EXCEED 85°C or eggs scramble!")
        
        while True:
            try:
                temp_input = input("\nEnter final temperature (°C): ").strip()
                temp = float(temp_input)
                self.batch_log['custard_final_temp'] = temp
                
                if temp < 80:
                    print("⚠️  Temperature too low - may not be safe or thick enough")
                elif 82 <= temp <= 84:
                    print("✅ Perfect temperature range!")
                elif temp <= 86:
                    print("⚠️  A bit high but should be okay")
                else:
                    print("⚠️  Too hot - eggs may have scrambled")
                
                break
            except ValueError:
                print("Please enter a valid number!")
        
        print("\n6. Remove from heat immediately")
        print("✅ Step 3 complete!")
    
    def _step4_chilling(self):
        """Step 4: Chill the base"""
        print("\n" + "="*60)
        print("STEP 4: CHILL HARD (4-24 hours)")
        print("="*60)
        
        print("\nInstructions:")
        print("1. Optional: Strain through fine-mesh strainer")
        print("2. Prepare ice bath (large bowl with ice + water)")
        print("3. Place pot in ice bath, stir occasionally for 30 min")
        print("4. Transfer to container, cover with plastic wrap")
        print("5. Refrigerate minimum 4 hours, ideally overnight")
        
        while True:
            try:
                chill_input = input("\nHow many hours will you chill? (recommended 12-24): ").strip()
                hours = float(chill_input)
                self.batch_log['chill_hours'] = hours
                
                if hours < 4:
                    print("⚠️  Less than 4 hours - may not churn well")
                elif hours >= 12:
                    print("✅ Excellent! Long chilling develops flavor")
                else:
                    print("✅ Should work, but longer is better")
                
                break
            except ValueError:
                print("Please enter a valid number!")
        
        print("\n⏱️  Chilling in progress...")
        print("(Come back when base is fully chilled)")
        print("✅ Step 4 complete!")
    
    def _step5_churning(self):
        """Step 5: Churn the gelato"""
        print("\n" + "="*60)
        print("STEP 5: CHURN (15-30 minutes) + ADD CHIPS")
        print("="*60)
        
        print("\nInstructions:")
        print("1. Ensure ice cream maker bowl is fully frozen")
        print("2. Pour chilled base into ice cream maker")
        print("3. Churn according to machine (usually 15-30 min)")
        print("4. Should reach soft-serve consistency")
        print("5. Optional: Add chocolate chips in last 1-2 minutes")
        
        while True:
            try:
                churn_input = input("\nHow many minutes did you churn? ").strip()
                minutes = int(churn_input)
                self.batch_log['churn_minutes'] = minutes
                
                if minutes < 15:
                    print("⚠️  Short churning - may be too soft")
                elif 15 <= minutes <= 30:
                    print("✅ Perfect churning time!")
                else:
                    print("⚠️  Long churning - check consistency")
                
                break
            except ValueError:
                print("Please enter a valid number!")
        
        print("✅ Step 5 complete!")
    
    def _step6_freezing(self):
        """Step 6: Freeze and serve"""
        print("\n" + "="*60)
        print("STEP 6: FREEZE + SERVE (2-4 hours)")
        print("="*60)
        
        print("\nInstructions:")
        print("1. Transfer gelato to freezer-safe container")
        print("2. Press plastic wrap directly on surface")
        print("3. Freeze 2-4 hours until firm but scoopable")
        print("4. SERVING: Let sit 5-10 min before scooping")
        print("   • Ideal serving temp: -12°C to -14°C (10-14°F)")
        print("   • Flavors are more pronounced when slightly soft")
        
        print("\n⏱️  Freezing in progress...")
        print("✅ Step 6 complete!")
    
    def _complete(self):
        """Complete the gelato making process"""
        print("\n" + "🎉" * 30)
        print("  GELATO COMPLETE!")
        print("🎉" * 30 + "\n")
        
        # Get rating and notes
        print("How did it turn out?")
        while True:
            try:
                rating_input = input("Rate your gelato (1-5 stars): ").strip()
                rating = int(rating_input)
                if 1 <= rating <= 5:
                    self.batch_log['rating'] = rating
                    break
                else:
                    print("Please enter a number between 1 and 5")
            except ValueError:
                print("Please enter a valid number!")
        
        notes = input("Any notes for next time? ").strip()
        self.batch_log['notes'] = notes
        
        # Save batch log
        self._save_batch_log()
        
        print("\n" + "="*60)
        print("BATCH SUMMARY:")
        print("="*60)
        print(f"Scale factor: {self.batch_log['scale_factor']}x")
        print(f"Mint steep time: {self.batch_log['mint_steep_time']} minutes")
        print(f"Custard temp: {self.batch_log['custard_final_temp']}°C")
        print(f"Chill time: {self.batch_log['chill_hours']} hours")
        print(f"Churn time: {self.batch_log['churn_minutes']} minutes")
        print(f"Rating: {'⭐' * self.batch_log['rating']}")
        if notes:
            print(f"Notes: {notes}")
        
        print("\n✨ Enjoy your homemade chocolate mint gelato! ✨")
        print("Batch log saved to gelato_batches.json\n")
    
    def _save_batch_log(self):
        """Save batch log to JSON file"""
        try:
            # Load existing logs
            try:
                with open('gelato_batches.json', 'r') as f:
                    logs = json.load(f)
            except FileNotFoundError:
                logs = []
            
            # Append new log
            logs.append(self.batch_log)
            
            # Save
            with open('gelato_batches.json', 'w') as f:
                json.dump(logs, f, indent=2)
                
        except Exception as e:
            print(f"Warning: Could not save batch log: {e}")


def main():
    """Main entry point"""
    maker = GelatoMaker()
    
    try:
        maker.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted! Your gelato making progress was not saved.")
        print("Come back when you're ready to make gelato! 🍦")
    except Exception as e:
        print(f"\n\n❌ An error occurred: {e}")
        print("Please report this issue on GitHub!")


if __name__ == "__main__":
    main()


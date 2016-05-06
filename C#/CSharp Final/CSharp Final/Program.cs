using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp_Final
{
    class Program
    {
        static void Main(string[] args)
        {

            using (var db = new SmashBrosContext())
            {
                
                var dict = CharacterAttacksData.AddCharacterAttacks();
                foreach(var pair in dict)
                {
                    db.Characters.Add(pair.Key);
                    db.Attacks.Add(pair.Value);
                }
                db.SaveChanges();
                

                Console.WriteLine("The following characters are playable in Super Smash Bros. for N64.");
                Console.WriteLine();

                var ShowCharacters = from characters in db.Characters
                            orderby characters.CharacterID
                            select characters;

                foreach(var character in ShowCharacters)
                {
                    Console.WriteLine(character.Name);
                }

                bool Loop = true;
                List<string> NameList = new List<string> {"Luigi", "Mario", "DK", "Link", "Samus", "Captain Falcon", "Ness", "Yoshi", "Kirby", "Fox", "Pikchu", "Jigglypuff" };
                

                while (Loop == true)
                {
                    Console.WriteLine();
                    Console.WriteLine("To view a character's special moves, type their name and press enter.");
                    Console.WriteLine("To exit, type 'Quit' and press enter.");
                    Console.WriteLine();
                    var name = Console.ReadLine();

                    if (NameList.Contains(name))
                    {
                        var ShowMoves = from characters in db.Characters
                                        join attacks in db.Attacks on characters.CharacterID equals attacks.CharacterID
                                        where name == characters.Name
                                        select new { attacks.UpB, attacks.NeutralB, attacks.DownB };

                        Console.WriteLine();
                        Console.WriteLine("{0} has the following special moves: ", name);

                        foreach (var move in ShowMoves)
                        {
                            Console.WriteLine(move);
                        }
                    }

                    else if (name == "Quit")
                    {
                        Loop = false;
                    }

                    else
                    {
                        Console.WriteLine();
                        Console.WriteLine("That name doesn't correspond to a playable character, try again!");
                    }
                    
                }
                
            }


            //Wait for user to acknowledge result
            Console.WriteLine();
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
                
        }
    }

    public class Character
    {
        [Key]
        public int CharacterID { get; set; }
        public string Name { get; set; }
        
        public virtual Attacks Attacks { get; set; }

    }

    public class Attacks
    {
        public string UpB {get; set;}
        public string NeutralB { get; set; }
        public string DownB { get; set; }
       
        [Key, ForeignKey("Character")]
        public int CharacterID { get; set; }
        public virtual Character Character { get; set; }

    }

    public class SmashBrosContext : DbContext
    {
        public DbSet<Character> Characters { get; set; }
        public DbSet<Attacks> Attacks { get; set; }
    }

    public class CharacterAttacksData
    {
        public static Dictionary<Character,Attacks> AddCharacterAttacks()
        {

            Character Luigi = new Character { Name = "Luigi", CharacterID = 1 };
            Attacks LuigiAttacks = new Attacks { UpB = "Fire Uppercut", NeutralB = "Green Fireball", DownB = "Tornado Spin", CharacterID = 1 };

            Character Mario = new Character { Name = "Mario", CharacterID = 2 };
            Attacks MarioAttacks = new Attacks { UpB = "Coin Uppercut", NeutralB = "Fireball", DownB = "Tornado Spin", CharacterID = 2 };

            Character DK = new Character { Name = "DK", CharacterID = 3 };
            Attacks DKAttacks = new Attacks { UpB = "Spinning Kong", NeutralB = "Giant Punch", DownB = "Ground Slap", CharacterID = 3 };

            Character Link = new Character { Name = "Link", CharacterID = 4 };
            Attacks LinkAttacks = new Attacks { UpB = "Spinning Slash", NeutralB = "Boomerang", DownB = "Bomb", CharacterID = 4 };

            Character Samus = new Character { Name = "Samus", CharacterID = 5 };
            Attacks SamusAttacks = new Attacks { UpB = "Screw Attack", NeutralB = "Charge Shot", DownB = "Bomb Drop", CharacterID = 5 };

            Character CaptainFalcon = new Character { Name = "Captain Falcon", CharacterID = 6 };
            Attacks CaptainFalconAttacks = new Attacks { UpB = "Falcon Dive", NeutralB = "Falcon Punch", DownB = "Falcon Kick", CharacterID = 6 };

            Character Ness = new Character { Name = "Ness", CharacterID = 7 };
            Attacks NessAttacks = new Attacks { UpB = "PK Thunder", NeutralB = "PK Fire", DownB = "PSI Magnet", CharacterID = 7};

            Character Yoshi = new Character { Name = "Yoshi", CharacterID = 8 };
            Attacks YoshiAttacks = new Attacks { UpB = "Egg Throw", NeutralB = "Lay Egg", DownB = "Ground Pound", CharacterID = 8 };

            Character Kirby = new Character { Name = "Kirby", CharacterID = 9 };
            Attacks KirbyAttacks = new Attacks { UpB = "Final Cutter", NeutralB = "Inhale", DownB = "Stone", CharacterID = 9 };

            Character Fox = new Character { Name = "Fox", CharacterID = 10 };
            Attacks FoxAttacks = new Attacks { UpB = "Fire Fox", NeutralB = "Laser Beam", DownB = "Shine Shield", CharacterID = 10 };

            Character Pikachu = new Character { Name = "Pikachu", CharacterID = 11 };
            Attacks PikachuAttacks = new Attacks { UpB = "Quick Attack", NeutralB = "Thunder Jolt", DownB = "Thunder Spike", CharacterID = 11 };

            Character Jigglypuff = new Character { Name = "Jigglypuff", CharacterID = 12 };
            Attacks JigglypuffAttacks = new Attacks { UpB = "Sing", NeutralB = "Pound", DownB = "Rest", CharacterID = 12 };

            Dictionary<Character,Attacks > CharacterDict = new Dictionary<Character, Attacks>
            {
                {Luigi, LuigiAttacks },
                {Mario, MarioAttacks },
                {DK, DKAttacks },
                {Link, LinkAttacks },
                {Samus, SamusAttacks },
                {CaptainFalcon, CaptainFalconAttacks },
                {Ness, NessAttacks },
                {Yoshi, YoshiAttacks },
                {Kirby, KirbyAttacks },
                {Fox, FoxAttacks },
                {Pikachu, PikachuAttacks },
                {Jigglypuff, JigglypuffAttacks }
            };

            return CharacterDict;
        }
        
    }
}

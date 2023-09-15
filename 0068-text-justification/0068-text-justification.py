class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_length = 0

        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                spaces_to_add = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces_to_add)
                else:
                    extra_spaces = spaces_to_add % (len(line) - 1)
                    space_per_gap = spaces_to_add // (len(line) - 1)
                    line_str = ''
                    for i in range(len(line) - 1):
                        line_str += line[i] + ' ' * (space_per_gap + (i < extra_spaces))
                    line_str += line[-1]
                    result.append(line_str)
                
                line = [word]
                line_length = len(word)

        # Handle the last line
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result

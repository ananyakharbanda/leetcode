class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        final = []
        toadd = []
        curr_length = 0

        for word in words:
            if curr_length + len(toadd) + len(word) > maxWidth:
                spaces_needed = maxWidth - curr_length
                if len(toadd) == 1:
                    final.append(toadd[0] + ' ' * spaces_needed)
                else:
                    space_between = spaces_needed // (len(toadd) - 1)
                    extra_spaces = spaces_needed % (len(toadd) - 1)

                    for i in range(extra_spaces):
                        toadd[i] += ' '  

                    final.append((' ' * space_between).join(toadd))

                toadd = []
                curr_length = 0

            toadd.append(word)
            curr_length += len(word)

        last_line = ' '.join(toadd)
        last_line += ' ' * (maxWidth - len(last_line))  
        final.append(last_line)

        return final

#alpha beta pruning

import chess
import copy
import numpy as np

def alpha_beta_search(alpha_pos, beta_pos, curr, max_depth=6, white):
    if max_depth == 0:
        return curr
    
    if white == True:
        first = False
        for move in curr.legal_moves:
            new_node = copy.deepcopy(curr)
            new_node.push(move)
            if first == False:
                leaf = alpha_beta_search(alpha_pos, beta_pos, new_node, max_depth-1, False)
                first = True
            if alpha_pos == 0:
                alpha_pos = leaf
            second = alpha_beta_search(alpha_pos, beta_pos, new_node, max_depth-1, False)
            output = prediction(leaf, second)
            if output == np.array([1,0]):
                better = leaf
            else:
                better = second
            output2 = prediction(alpha_pos, better)
            if output == np.array([1,0]):
                pass
            else:
                alpha_pos = better
            if beta_pos != 0:
                final = prediction(alpha_pos, beta_pos)
                if final == np.array([1,0]):
                    break
        return better
            
    else:
        first = False
        for move in curr.legal_moves:
            new_node = copy.deepcopy(curr)
            new_node.push(move)
            if first == False:
                leaf = alpha_beta_search(alpha_pos, beta_pos, new_node, max_depth-1, True)
                first = True
            if beta_pos == 0:
                beta_pos = leaf
            second = alpha_beta_search(alpha_pos, beta_pos, new_node, max_depth-1, True)
            output = prediction(leaf, second)
            if output == np.array([0,1]):
                better = leaf
            else:
                better = second
            output2 = prediction(beta_pos, better)
            if output2 == np.array([0,1]):
                pass
            else:
                beta_pos = better
            if alpha_pos != 0:
                final = prediction(alpha_pos, beta_pos)
                if final == np.array([1,0]):
                    break
        return better



def prediction(pos1, pos2):
    pos1bit = pos1.bit_encode()
    pos2bit = pos2.bit_encode()
    return
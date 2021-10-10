# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/09 18:15:09 by cacharle          #+#    #+#              #
#    Updated: 2021/10/10 22:21:08 by tayamamo         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from c_formatter_42.formatters.align import align
from c_formatter_42.formatters.clang_format import clang_format
from c_formatter_42.formatters.hoist import hoist
from c_formatter_42.formatters.misc import (parenthesize_return,
                                            remove_multiline_condition_space,
                                            space_before_semi_colon)
from c_formatter_42.formatters.preprocessor_directive import \
    preprocessor_directive


def run_all(content: str) -> str:
    """ Run all formatters """
    content = clang_format(content)
    content = preprocessor_directive(content)
    content = remove_multiline_condition_space(content)
    content = parenthesize_return(content)
    content = space_before_semi_colon(content)
    content = hoist(content)
    content = align(content)
    return content

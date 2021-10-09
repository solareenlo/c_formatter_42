# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/09 18:15:09 by cacharle          #+#    #+#              #
#    Updated: 2021/10/10 00:42:57 by tayamamo         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from c_formatter_42.formatters.misc import (
    parenthesize_return,
    space_before_semi_colon,
    remove_multiline_condition_space
)
from c_formatter_42.formatters.preprocessor_directive import preprocessor_directive
from c_formatter_42.formatters.clang_format import clang_format
from c_formatter_42.formatters.hoist import hoist
from c_formatter_42.formatters.align import align


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

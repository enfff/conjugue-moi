#!/usr/bin/bash

options="hab:c"
while getopts $options opt; do
	case $opt in
	h)
	echo "help thingy"
	;;
	a)
	echo "option -a"
	;;
	b)
	arg=$OPTARG
	echo "option -b, hai passato $arg"
	;;
	c)
	echo "option -c"
	;;
	\?)
	echo "invalid option"
	;;
	esac
done

user_input = 0
correct_value

function compare_user_input_with_correct_value {
#   commands
}

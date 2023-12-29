import scrap
import workflow
from main_p1 import process_full_scrap
from main_p1 import solve as p1_solve

# from main_p2 import solve as p2_solve

lines = [
    "px{a<2006:qkq,m>2090:A,rfg}",
    "pv{a>1716:R,A}",
    "lnx{m>1548:A,A}",
    "rfg{s<537:gd,x>2440:R,A}",
    "qs{s>3448:A,lnx}",
    "qkq{x<1416:A,crn}",
    "crn{x>2662:A,R}",
    "in{s<1351:px,qqz}",
    "qqz{s>2770:qs,m<1801:hdj,R}",
    "gd{a>3333:R,R}",
    "hdj{m>838:A,pv}",
    "",
    "{x=787,m=2655,a=1222,s=2876}",
    "{x=1679,m=44,a=2067,s=496}",
    "{x=2036,m=264,a=79,s=2244}",
    "{x=2461,m=1339,a=466,s=291}",
    "{x=2127,m=1623,a=2188,s=1013}",
]

current_scrap = scrap.from_string("{x=5,m=5,a=5,s=5}")


def test_p1():
    assert p1_solve(lines) == 19114


def test_approval_via_condition():
    current_workflow = {"in": workflow.wf_from_string("in{s>1:A,qqz}")}
    assert process_full_scrap(current_scrap, current_workflow)


def test_approval_via_default():
    current_workflow = {
        "in": workflow.wf_from_string("in{s<1:abc,A}"),
        "abc": workflow.wf_from_string("abc{s>1:R,R}"),
    }
    assert process_full_scrap(current_scrap, current_workflow)


def test_rejection_via_condition():
    current_workflow = {"in": workflow.wf_from_string("in{s>1:R,qqz}")}
    assert not process_full_scrap(current_scrap, current_workflow)


def test_rejection_via_default():
    current_workflow = {
        "in": workflow.wf_from_string("in{s<1:abc,R}"),
        "abc": workflow.wf_from_string("abc{s>1:A,A}"),
    }
    assert not process_full_scrap(current_scrap, current_workflow)


def test_approval_via_condition_in_sub():
    current_workflow = {
        "in": workflow.wf_from_string("in{s>1:abc,R}"),
        "abc": workflow.wf_from_string("abc{s>1:A,R}"),
    }
    assert process_full_scrap(current_scrap, current_workflow)


# def test_p2():
#     assert p2_solve(lines) == 952408144115

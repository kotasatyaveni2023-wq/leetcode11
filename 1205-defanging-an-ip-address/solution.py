class Solution:
    def defangIPaddr(self, address: str) -> str:
        llist1=address.split(".")
        return "[.]".join(llist1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        total = len(A) + len(B)        
        l = 0
        r = len(A) -1
        while True:
            mid = (l + r) // 2
            Bindex = total // 2 - mid - 2

            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid + 1] if mid + 1 < len(A) else float("infinity")
            
            Bleft = B[Bindex] if Bindex >= 0 else float("-infinity")
            Bright = B[Bindex + 1] if Bindex + 1 < len(B) else float("infinity")

            if Aright >= Bleft and Aleft <= Bright:
                if total % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            else:
                if Aleft > Bright:
                    r = mid -1
                else:
                    l = mid + 1
        return -1
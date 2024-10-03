# Slider

def max_sub_array(nums):
    current_sum=max_sum=nums[0]
    for num in nums[1:]:
        current_sum=max(num, current_sum+num)
        max_sum=max(max_sum, current_sum)

    return max_sum

nums=[1,-2,2,4,7,4,-3,-8]
print("Maximum subarray=", max_sub_array(nums))


# Merge Sort

def merge_sort(nums):
    if len(nums)>1:
        mid=len(nums)//2
        left_half=nums[:mid]
        right_half=nums[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=j=k=0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                nums[k]=left_half[i]
                i+=1
            else:
                nums[k]= right_half[j]
                j+=1
            k+=1
        while i<len(left_half):
                nums[k]=left_half[i]
                i+=1
                k+=1

        while j<len(right_half):
                nums[k]=right_half[j]
                j+=1
                k+=1
nums=[23,56,4,3,78,4, 4]
merge_sort(nums)
print("merged sort=", nums)

#Duplicate 
def removeDuplicate(nums):
    if not nums:
        return 0
    
    i=0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]

    return i+1
        
nums1=[1,1,2,3,3,3,5,6,6]
r1=removeDuplicate(nums1)
print("The answer is: ",r1)
print("The updated list is", nums1[:r1])




   
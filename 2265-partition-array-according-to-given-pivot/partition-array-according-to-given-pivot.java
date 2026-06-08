class Solution 
{
    public int[] pivotArray(int[] nums, int pivot)
    {
        int l = nums.length;
        int[] arr = new int[l];
        int k = 0;
        for(int i=0;i<l;i++){
            if (nums[i] < pivot){
                arr[k] = nums[i];
                k++;
            }
        }
        for(int i=0;i<l;i++){
            if (nums[i] == pivot){
                arr[k] = nums[i];
                k++;
            }
        }
        for(int i=0;i<l;i++){
            if (nums[i] > pivot){
                arr[k] = nums[i];
                k++;
            }
        }
        return arr;

    }
}
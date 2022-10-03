/*
    Implementation of dynamically resizable array in C++
    Like vector class defined in vector.h
    TODO: add more datatype support using templates

    This may help you to get the idea of how 
    vectors work under then hood in C++
*/

#include <iostream>
 
class DynamicArray 
{
public:
    DynamicArray()
    {
        // initalizes the heap allocated array
        // with max size: 8
        // index: 0
        // increment size: 32
        init(8, 0, 32);
    }

    DynamicArray(int defaultSize)
    {
        init(defaultSize, 0, 32);
    }

    /// @brief Get the size of array
    /// @return the size
    size_t size()
    {
        return m_curIndex;
    }


    /// @brief Gets the max capacity of array
    /// @return The max capacity of array
    size_t capacity()
    {
        return m_maxSize;
    }


    /// @brief Gets the total 
    /// @return The total memory consumed by the array, in bytes
    size_t total_mem_consumed()
    {
        return m_maxSize * sizeof(int);
    }


    /// @brief Gets the element at index 'i' of the array
    /// @param i The elements index
    /// @return The element
    int& operator[] (size_t i)
    {
        if (i > m_curIndex)
        {
            std::cout << "Index out of bounds!" << std::endl;
        }
        return m_array[i];
    }

    /// @brief Pushes an new elemnt to the end of the array
    /// @param data The data to add into the array
    void push_back(int data)
    {
        /* 
            When current index gets more than the capacity of array
            increase the max capacity of array and 
            relalocate the memory
        */
        if (m_curIndex > m_maxSize)
        {
            m_maxSize += m_incrementCount;
            m_array = (int*)realloc(m_array, m_maxSize * sizeof(int));

            if (m_array == NULL)
            {
                std::cout << "Error initalizing memory for new array size!" << std::endl;
                return;
            }
        }

        // add new element to the array
        m_array[m_curIndex] = data;
        ++m_curIndex;
    }


    void set_max_size(size_t max)
    {
        if (max < m_maxSize)
        {
            std::cout << "The max is less than the current max capacity of the array!" << std::endl;
            return;
        }
        m_maxSize = max;
    }


    ~DynamicArray()
    {
        // clears up the memory taken by the array
        delete[] m_array;
        m_curIndex = 0;
        m_maxSize = 0;
    }
    
private:
    void init(int max, int cur, int increm)
    {
        m_maxSize = max;
        m_curIndex = cur;
        m_incrementCount = increm; // Increments the array size by increm*4 bytes each time
        m_array = (int*)malloc(sizeof(int) * m_maxSize);
    }

private:
    int m_curIndex;
    int m_maxSize;
    int m_incrementCount;
    int *m_array;
};

int main()
{   
    DynamicArray arr;

    for (int i = 0; i < 10; i++)
    {
        arr.push_back(i);
    }
    

    for (int i = 0; i < arr.size(); i++)
    {
        std::cout << arr[i] << std::endl;
    }
    

}
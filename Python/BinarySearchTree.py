#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 11:36:12 2022

@author: rik
"""


class Tree():
    
    class Position():
        
        def element(self):
            raise NotImplementedError('must be implemented by a subclass')
        def __eq__(self):
            raise NotImplementedError('must be implemented by a subclass')
        def __ne__(self,other):
            
            return not(self==other)
        def root(self):
            raise NotImplementedError('must be implemented by a subclass')
            
        def parent(self,p):
            
            raise NotImplementedError('must be implemented by a subclass')
        def num_children(self,p):
            raise NotImplementedError('must be implemented by a subclass')
        def children(self,p):
            raise NotImplementedError('must be implemented by a subclass')
        def __len__(self):
            raise NotImplementedError('must be implemented by a subclass')
        def __iter__(self):
            for p in self.positions():
                yield p.element()
        
        
        
        def is_root(self,p):
            return self.root()==p
        def is_leaf(self,p):
            return self.num_children(p)==0
        def is_empty(self):
            return len(self)==0
    
        def depth(self,p):
            if self.is_root(p):
                return 0
            else:
                return 1+self.depth(self.parent(p))
            
        def _height2(self,p):
            if self.is_leaf(p):
                return 0
            else:
                return 1+max(self._height2(c) for c in self.children(p))
            
        def height(self,p=None):
            if p is None:
                p=self.root()
                return self._height2(p)
            
        def preorder(self):
            if not self.is_empty():
                for p in self._subtree_preorder(self.root()):
                    yield p
                    
                    
        def postorder(self):
            if not self.is_empty():
                for p in self._subtree_postorder(self.root()):
                    yield p
        def _subtree_postorder(self,p):
            for c in self.children(p):
                for other in self._subtree_postorder(c):
                    yield other
                    
            yield p
            
        def _subtree_preorder(self,p):
            yield p
            for c in self.children(p):
                for other in self._subtree_preorder(c):
                    yield other
        def positions(self):
            return self.preorder()
                    
        
            

class BinaryTree(Tree):
    
    def left(self,p):
        
        raise NotImplementedError('must be implemented by a subclass')
    def right(self,p):
        raise NotImplementedError('must be implemented by a subclass')
    def sibling(self,p):
        parent=self.parent(p)
        if parent is None:
            return None
        else:
            if p==self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
            
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:18:16 2022

@author: rik
"""

class LinkedBinaryTree(BinaryTree):
    
    class _Node():
        __slots__='_element','_parent','_right','_left'
        def __init__(self,element,parent,right,left):
            self._element=element
            self._parent=parent
            self._right=right
            self._left=left
    class Position(BinaryTree.Position):
        
        def __init__(self,container,node):
            self._container=container
            self._node=node
        def element(self):
            return self._node._element
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        def _validate(self,p):
            if not isinstance(p,self.Position):
                raise TypeError(' p must be proper position type')
            if p._container is not self:
                raise ValueError(' p does not belong to this container')
            if p._node._parent is p._node:
                raise ValueError('p is deprecated')
            return p._node
            
        def _make_position(self,node):
            
            return self.Position(self,node) if node is not None else None
        
    def __init__(self):
        self._root=None
        self._size=0
    def __len__(self):
        return self._size
    def root(self):
        return self._make_position(self.root)
    def parent(self,p):
        node=self._validate(p)
        return self._make_position(node._parent)
    def left(self,p):
        node=self._validate(p)
        return self._make_position(node._left)
    def right(self,p):
        node=self._validate(p)
        return self._make_position(node._right)
    def num_children(self,p):
        node=self._validate(p)
        count=0
        if node._left is not None:
            count+=1
        if node._right is not None:
            count+=1
            
        return count
    
    def _add_root(self,e):
        if self._root is not None: raise ValueError('root already exists')
        self._size=1
        self._root=self._Node(e)
        return self._make_position(self._root)
    def _add_left(self,e):
        node=self._validate(e)
        if node._left is not None: raise ValueError('left child already exists')
        self._size+=1
        node._left=self._Node(e,node)
        return self._make_position(node._left)
    
    def _add_right(self,e):
        node=self._validate(e)
        if node._right is not None: raise ValueError('right child already exists')
        self._size+=1
        node._right=self._Node(e,node)
        return self._make_position(node._right)
    
        
        
    def _replace(self,p,e):
        node=self._validate(p)
        old=node._element
        node._element=e
        return old
    def _delete(self,p):
        node=self._validate(p)
        if self.num_children(p)==2: raise ValueError('p has two children')
        child=node._left if node._left else node._right
        if child is not None:
            child._parent=node._parent
        if node is self._root:
            self._root=child
        else:
            parent=node._parent
            if node is parent._left:
                parent._left=child
            else:
                parent._right=child
        self._size-=1 
        node._parent=node
        return node._element
    def _attach(self, p, t1,t2):

        node=self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('all trees must be concordant types')
        self._size+=len(t1)+len(t2)
        if not t1.is_empty():
            t1._root._parent=node
            node._left=t1._root
            t1._root=None
            t1._size=0
        if not t2.is_empty():
            t2._root._parent=node
            node._left=t1._root
            t2._root=None
            t2._size=0

from collections import MutableMapping


class Mapbase(MutableMapping):
    class _Item:
        __slots__='_key','_value'
        
        def __init__(self,k,v):
            self._key=k
            self._value=v
            
        def __eq__(self,other):
            return self._key==other._key
        def __ne__(self,other):
            return not(self==other)
        def __It__(self,other):
            return self._key<other._key
        
    
class BinarySearchTree(Mapbase,LinkedBinaryTree):
    
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key
        def value(self):
            return self.element()._value
        
    def _subtree_search(self,p,k):
        if k==p.key():
            return p
        elif k<p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p),k)
        else:
            if  self.right(p) is not None:
                return self._subtree_search(self.right(p),k)
        return p
    
    def _subtree_first_position(self,p):
        walk=p
        while self.left(walk) is not None:
            walk=self.left(walk)
        return walk
    def _subtree_last_position(self,e):
        walk=e
        while self.right(walk) is not None:
            walk=self.right(walk)
        return walk
    def first(self):
        return self._subtree_first_position(self.root()) if len(self)>0 else None
    def last(self):
        return self._subtree_last_position(self.root()) if len(self)>0 else None
    def before(self,p):
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk=p
            above=self.parent(walk)
            while above is not None and walk==self.left(above):
               walk=above
               above=self.parent(walk)
            return above
        
    def after(self,p):
        self.validate(p)
        if self.right(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk=p
            above=self.parent(walk)
            while above is not None and walk==self.left(above):
                walk=above
                above=self.parent(walk)
            return above
    
    
    def find_position(self,k):
        if self.is_empty():
            return None
        else:
            p=self._subtree_search(self.root(),k)
            self._rebalance_access(p)
            return p
        
        
    def find_min(self):
        if self.is_empty():
            return None
        else:
            p=self.first()
            return (p.key(),p.value())
        
    def find_ge(self,k):
        if self.is_empty():
            return None
        else:
            p=self.find_position(k)
            if p.key()<k:
                p=self.after(p)
            return (p.key(),p.value()) if p is not None else None
    
    def find_range(self,start,stop):
        
        if self.is_empty():
            if start is None:
                p=self.first()
            else:
                p=self.find_position(start)
                if p.key()<start:
                    p=self.after(p)
            while p is not None and (stop is None or p.key()<stop):
                yield (p.key(),p.value())
                p=self.after(p)
                
        
    def __getitem__(self,k):
        
        if self.is_empty():
            raise KeyError('Key Error'+repr(k))
            
        else:
            p=self._subtree_search(self.root(),k)
            self._rebalance_access(p)
            if k!=p.key():
                raise KeyError('Key Error'+repr(k))
            return p.value()
        
    def __setitem__(self,k,v):
        if self.is_empty():
            leaf=self._add_root(self._Item(k,v))
        else:
            p=self._subtree_search(self.root(),k)
            if p.key()==k:
                p.element()._value=v
                self._rebalance_access(p)
                return
            else:
                item=self._Item(k,v)
                if p.key()<k:
                    leaf=self._add_right(p,item)
                else:
                    leaf=self._add_left(p,item)
                    
        self._rebalance_insert(leaf)
            
        
    def __iter__(self):
        p=self.first()
        while p is not None:
            yield p.key()
            p=self.after(p)
            
            
    def delete(self,p):
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement=self._subtree_last_position(self.left(p))
            self._replace(p,replacement.element())
            p=replacement
        parent=self._parent(p)
        self.delete(p)
        self._rebalance_delete(parent)
        
    def __delitem__(self,k):
        if not self.is_empty():
            p=self._subtree_search(self.root(),k)
            if k==p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
            raise KeyError('Key Erro'+repr(k))
                  
        
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
